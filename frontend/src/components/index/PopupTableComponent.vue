<template>
  <q-toolbar>
    <q-toolbar-title>Pop-ups Programados ({{ rows.length || '0' }})</q-toolbar-title>
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
    :rows="rows"
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
            <q-card-section class="col-xs-12 col-sm-3 col-md-2">
              <q-img
                class="rounded-borders"
                ratio="1"
                src="https://cdn.quasar.dev/img/parallax2.jpg"
              />
            </q-card-section>
            <q-card-section class="col">
              <div><q-badge class="text-bold q-pa-xs">Programado</q-badge></div>
              <div class="text-h5 q-mt-sm q-mb-xs">{{ props.row.name }}</div>

              <div class="text-caption">
                {{ props.row.description }}
              </div>

              <div class="row q-gutter-x-lg q-mt-sm">
                <div><q-icon name="event"></q-icon> 01 nov 2025</div>
                <div><q-icon name="alarm"></q-icon> 09:00 AM</div>
                <div><q-icon name="desktop_windows"></q-icon> Todos los dispositivos</div>
              </div>
            </q-card-section>

            <q-card-actions vertical>
              <q-btn flat round icon="more_vert">
                <q-menu>
                  <q-list style="min-width: 200px">
                    <q-item clickable v-close-popup class="text-primary">
                      <q-item-section avatar><q-icon name="preview"></q-icon></q-item-section>

                      <q-item-section>Previsualizar</q-item-section>
                    </q-item>

                    <q-item clickable v-close-popup class="text-secondary">
                      <q-item-section avatar><q-icon name="edit"></q-icon></q-item-section>

                      <q-item-section>Editar</q-item-section>
                    </q-item>

                    <q-separator></q-separator>

                    <q-item clickable v-close-popup class="text-negative">
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
import { defineComponent, ref } from 'vue';

export default defineComponent({
  name: 'PopupTableComponent',

  setup() {
    const filter = ref('');

    const rows = ref([
      {
        id: '1',
        name: 'Actualización de Seguridad Importante',
        description:
          'Se requiere reiniciar su computadora para aplicar las actualizaciones de seguridad críticas. Por favor, guarde su trabajo y reinicie antes del fin del día.',
      },
      {
        id: '2',
        name: 'Actualización de Seguridad Importante',
        description:
          'Se requiere reiniciar su computadora para aplicar las actualizaciones de seguridad críticas. Por favor, guarde su trabajo y reinicie antes del fin del día.',
      },
      {
        id: '3',
        name: 'Actualización de Seguridad Importante',
        description:
          'Se requiere reiniciar su computadora para aplicar las actualizaciones de seguridad críticas. Por favor, guarde su trabajo y reinicie antes del fin del día.',
      },
      {
        id: '4',
        name: 'Actualización de Seguridad Importante',
        description:
          'Se requiere reiniciar su computadora para aplicar las actualizaciones de seguridad críticas. Por favor, guarde su trabajo y reinicie antes del fin del día.',
      },
      {
        id: '5',
        name: 'Actualización de Seguridad Importante',
        description:
          'Se requiere reiniciar su computadora para aplicar las actualizaciones de seguridad críticas. Por favor, guarde su trabajo y reinicie antes del fin del día.',
      },
      {
        id: '6',
        name: 'Actualización de Seguridad Importante',
        description:
          'Se requiere reiniciar su computadora para aplicar las actualizaciones de seguridad críticas. Por favor, guarde su trabajo y reinicie antes del fin del día.',
      },
    ]);
    return { filter, rows };
  },
});
</script>
