<template>
  <q-toolbar>
    <q-toolbar-title
      >Dispositivos Conectados ({{ mainStore.devices.length || '0' }})</q-toolbar-title
    >
    <q-space></q-space>
    <q-input borderless dense debounce="300" v-model="filter" placeholder="Buscar...">
      <template v-slot:append>
        <q-icon name="search" />
      </template>
    </q-input>
  </q-toolbar>

  <q-table
    grid
    flat
    bordered
    :card-container-class="'cardContainerClass'"
    :rows="mainStore.devices"
    :columns="[
      { name: 'name', required: true, label: 'Nombre', align: 'left', field: 'name' },
      {
        name: 'description',
        required: true,
        label: 'Descripción',
        align: 'left',
        field: 'description',
      },
    ]"
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
        <q-card flat bordered>
          <q-card-section :horizontal="$q.screen.gt.xs" class="row q-pa-none">
            <q-card-section class="xs-hide">
              <q-avatar
                :color="props.row.status == 'ONLINE' ? 'positive' : 'grey'"
                text-color="white"
                :icon="props.row.deviceType == 'pc' ? 'desktop_windows' : 'laptop_windows'"
                size="xl"
              />
            </q-card-section>
            <q-card-section class="col">
              <div>
                <q-chip icon="account_tree">
                  {{
                    mainStore.dependencies.find(
                      (anyDependency) =>
                        anyDependency.identifier == props.row.dependency_identifier,
                    )?.name
                  }}
                </q-chip>

                <q-chip
                  outline
                  :color="props.row.status == 'ONLINE' ? 'green' : 'grey'"
                  icon="fiber_manual_record"
                >
                  {{ props.row.status == 'ONLINE' ? 'En línea' : 'Desconectado' }}
                </q-chip>
              </div>

              <div class="text-h5 q-mt-sm q-mb-xs">{{ props.row.name }}</div>

              <!-- <div class="text-caption">
                {{ props.row.description }}
              </div> -->

              <div class="row q-gutter-x-lg q-mt-sm">
                <!-- <div><q-icon name="person" /> {{ props.row.owner }}</div> -->
                <div>OS: {{ props.row.operating_system }}</div>
                <div>IP: {{ props.row.IP }}</div>

                <div>
                  Puerto:
                  {{ props.row.port }}
                </div>
              </div>

              <div class="text-grey">
                Última conexión: {{ props.row.last_connection.replace('T', ' ').split('.')[0] }}
              </div>
            </q-card-section>

            <q-card-actions vertical>
              <q-btn flat round icon="more_vert">
                <q-menu>
                  <q-list style="min-width: 200px">
                    <q-item clickable v-close-popup class="text-primary" disable>
                      <q-item-section avatar><q-icon name="preview"></q-icon></q-item-section>

                      <q-item-section>Previsualizar</q-item-section>
                    </q-item>

                    <q-item
                      clickable
                      v-close-popup
                      class="text-secondary"
                      @click="mainStore.setEditDeviceFormData({ ...props.row })"
                    >
                      <q-item-section avatar><q-icon name="edit"></q-icon></q-item-section>

                      <q-item-section>Editar</q-item-section>
                    </q-item>

                    <q-separator></q-separator>

                    <q-item
                      clickable
                      v-close-popup
                      class="text-negative"
                      @click="confirmDeleteDevice({ ...props.row })"
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
</template>

<script lang="ts">
import { useQuasar } from 'quasar';
import type { IDevice } from 'src/modules/interfaces/device';
import { useMainStore } from 'src/stores/main-store';
import { defineComponent, ref } from 'vue';

export default defineComponent({
  name: 'DevicesTableComponent',

  setup() {
    const $q = useQuasar();
    const filter = ref('');

    const mainStore = useMainStore();

    const loadingDependencyTable = ref(false);

    const handlerGetDevices = async () => {
      try {
        loadingDependencyTable.value = true;
        await mainStore.getDevices();
      } catch {
        //
      } finally {
        loadingDependencyTable.value = false;
      }
    };
    void handlerGetDevices();

    const handlerEditDevice = async () => {
      try {
        await mainStore.editDevice();
        $q.notify({
          message: 'Dispositivo editado',
          type: 'positive',
        });
      } catch {
        $q.notify({
          message: 'Error al editar dispositivo',
          type: 'negative',
        });
      }
    };

    const handlerDeleteDevice = async (deviceId: string) => {
      try {
        await mainStore.deleteDevice(deviceId);
        $q.notify({
          message: 'Dispositivo eliminado',
          type: 'positive',
        });
      } catch {
        $q.notify({
          message: 'Error al editar dispositivo',
          type: 'negative',
        });
      }
    };

    const confirmDeleteDevice = (deviceData: IDevice) => {
      $q.dialog({
        title: '¿Eliminar dispositivo?',
        message: deviceData.name,
        cancel: true,
        persistent: false,
      }).onOk(() => {
        if (deviceData.identifier) void handlerDeleteDevice(deviceData.identifier);
      });
    };

    return { filter, mainStore, handlerEditDevice, confirmDeleteDevice };
  },
});
</script>
