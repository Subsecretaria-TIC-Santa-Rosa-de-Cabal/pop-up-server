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
        <q-card flat bordered>
          <q-card-section :horizontal="$q.screen.gt.xs" class="row">
            <q-card-section class="col">
              <div class="text-h5">{{ props.row.name }}</div>
              <div><q-icon name="tv"></q-icon> Dispositivos - {{ props.row.deviceCount }}</div>
            </q-card-section>

            <q-card-actions vertical>
              <q-btn flat round icon="more_vert">
                <q-menu>
                  <q-list style="min-width: 200px">
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
import type { IDependency } from '../modules/interfaces/dependency';

export default defineComponent({
  name: 'DependencyTableComponent',

  setup() {
    const filter = ref('');

    const rows = ref<IDependency[]>([
      {
        identifier: '1',
        name: 'Dependencia 1',
        deviceCount: 1,
      },
      {
        identifier: '2',
        name: 'Dependencia 2',
        deviceCount: 1,
      },
      {
        identifier: '3',
        name: 'Dependencia 3',
        deviceCount: 1,
      },
      {
        identifier: '4',
        name: 'Dependencia 4',
        deviceCount: 1,
      },
      {
        identifier: '5',
        name: 'Dependencia 5',
        deviceCount: 1,
      },
      {
        identifier: '6',
        name: 'Dependencia 6',
        deviceCount: 1,
      },
      {
        identifier: '7',
        name: 'Dependencia 7',
        deviceCount: 1,
      },
      {
        identifier: '8',
        name: 'Dependencia 8',
        deviceCount: 1,
      },
      {
        identifier: '9',
        name: 'Dependencia 9',
        deviceCount: 1,
      },
    ]);
    return { filter, rows };
  },
});
</script>
