<template>
  <q-toolbar>
    <q-toolbar-title> Dependencias ({{ mainStore.dependencies.length || '0' }})</q-toolbar-title>
    <q-space></q-space>
    <q-input borderless dense debounce="300" v-model="filter" placeholder="Buscar...">
      <template v-slot:append>
        <q-icon name="search" />
      </template>
    </q-input>
  </q-toolbar>

  <q-table
    :loading="loadingDependencyTable"
    grid
    flat
    bordered
    :card-container-class="'cardContainerClass'"
    :rows="mainStore.dependencies"
    :columns="[{ name: 'name', required: true, label: 'Nombre', align: 'left', field: 'name' }]"
    row-key="name"
    :filter="filter"
    :pagination="{
      sortBy: 'name',
      descending: false,
      page: 1,
      rowsPerPage: 0,
    }"
    hide-header
    hide-bottom
  >
    <template v-slot:item="props">
      <div class="q-pa-xs col-xs-12 col-sm-12 col-md-12 col-lg-6">
        <q-card
          flat
          bordered
          :class="mainStore.dependencyFormData.identifier == props.row.identifier && 'bg-secondary'"
        >
          <q-card-section :horizontal="$q.screen.gt.xs" class="row">
            <q-card-section class="col">
              <div class="text-h5">{{ props.row.name }}</div>
              <div><q-icon name="tv"></q-icon> Dispositivos - {{ props.row.devices_count }}</div>
            </q-card-section>

            <q-card-actions vertical>
              <q-btn flat round icon="more_vert">
                <q-menu>
                  <q-list style="min-width: 200px">
                    <q-item
                      clickable
                      v-close-popup
                      class="text-secondary"
                      @click="mainStore.setEditDependencyFormData({ ...props.row })"
                    >
                      <q-item-section avatar><q-icon name="edit"></q-icon></q-item-section>

                      <q-item-section>Editar</q-item-section>
                    </q-item>

                    <q-separator></q-separator>

                    <q-item
                      clickable
                      v-close-popup
                      class="text-negative"
                      @click="confirmDeleteDependency(props.row)"
                      :disable="props.row.devices_count > 0"
                    >
                      <q-item-section avatar><q-icon name="delete"></q-icon></q-item-section>

                      <q-item-section>Eliminar</q-item-section>
                    </q-item>
                  </q-list>
                </q-menu>
              </q-btn>
            </q-card-actions>
          </q-card-section>
        </q-card>
      </div>
    </template>
  </q-table>

  <!-- <q-dialog v-model="mainStore.showDependencyEditForm">
    <q-card>
      <q-card-section>
        <div class="text-bold text-h6 q-mb-md">Editar Dependencia</div>

        <q-form @submit.prevent="handlerEditDependency">
          <DependencyFormComponent />
          <div class="q-mt-md">
            <q-btn
              class="full-width"
              color="primary"
              label="Registrar dependencia"
              type="submit"
            ></q-btn>
          </div>
        </q-form>
      </q-card-section>
    </q-card>
  </q-dialog> -->
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { useQuasar } from 'quasar';

import { useMainStore } from 'src/stores/main-store';
import type { IDependency } from 'src/modules/interfaces/dependency';

export default defineComponent({
  name: 'DependencyTableComponent',

  components: {
    //
  },

  setup() {
    const $q = useQuasar();
    const filter = ref('');

    const mainStore = useMainStore();

    const loadingDependencyTable = ref(false);

    const handlerGetDependency = async () => {
      try {
        loadingDependencyTable.value = true;
        await mainStore.getDependencies();
      } catch {
        //
      } finally {
        loadingDependencyTable.value = false;
      }
    };
    void handlerGetDependency();

    const handlerEditDependency = async () => {
      try {
        await mainStore.editDependency();
        $q.notify({
          message: 'Dependencia editada',
          type: 'positive',
        });
      } catch {
        $q.notify({
          message: 'Error al editar dependencia',
          type: 'negative',
        });
      }
    };

    const handlerDeleteDependency = async (dependencyId: string) => {
      try {
        await mainStore.deleteDependency(dependencyId);
        $q.notify({
          message: 'Dependencia eliminada',
          type: 'positive',
        });
      } catch {
        $q.notify({
          message: 'Error al editar dependencia',
          type: 'negative',
        });
      }
    };

    const confirmDeleteDependency = (dependencyData: IDependency) => {
      $q.dialog({
        title: '¿Eliminar dependencia?',
        message: dependencyData.name,
        cancel: true,
        persistent: false,
      }).onOk(() => {
        void handlerDeleteDependency(dependencyData.identifier);
      });
    };

    return {
      filter,

      mainStore,
      loadingDependencyTable,

      handlerGetDependency,
      handlerEditDependency,
      confirmDeleteDependency,
    };
  },
});
</script>
