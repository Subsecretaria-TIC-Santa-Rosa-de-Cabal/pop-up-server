<template>
  <q-toolbar>
    <q-toolbar-title>Dispositivos Conectados ({{ rows.length || '0' }})</q-toolbar-title>
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
      <div class="q-pa-xs col-xs-12 col-sm-12 col-md-6">
        <q-card flat bordered>
          <q-card-section :horizontal="$q.screen.gt.xs" class="row q-pa-none">
            <q-card-section class="xs-hide">
              <q-avatar
                :color="props.row.online ? 'positive' : 'grey'"
                text-color="white"
                :icon="props.row.deviceType == 'pc' ? 'desktop_windows' : 'laptop_windows'"
                size="xl"
              />
            </q-card-section>
            <q-card-section class="col">
              <div>
                <q-chip icon="account_tree"> Despacho del alcalde </q-chip>

                <q-chip
                  outline
                  :color="props.row.online ? 'green' : 'grey'"
                  icon="fiber_manual_record"
                >
                  {{ props.row.online ? 'En línea' : 'Desconectado' }}
                </q-chip>
              </div>

              <div class="text-h5 q-mt-sm q-mb-xs">{{ props.row.name }}</div>

              <!-- <div class="text-caption">
                {{ props.row.description }}
              </div> -->

              <div class="row q-gutter-x-lg q-mt-sm">
                <div><q-icon name="person" /> {{ props.row.owner }}</div>
                <div>OS - {{ props.row.os }}</div>
                <div>IP - {{ props.row.ip }}</div>
                <div><q-icon name="location_on" /> {{ props.row.location }}</div>
                <div>
                  <q-icon
                    :name="props.row.deviceType == 'pc' ? 'desktop_windows' : 'laptop_windows'"
                  />
                  {{ props.row.deviceType }}
                </div>
              </div>

              <div class="text-grey q-mt-md">
                <q-icon name="event" /> {{ props.row.lastConnection }}
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
  name: 'DevicesTableComponent',

  setup() {
    const filter = ref('');

    const rows = ref([
      {
        id: '1',
        name: 'PC-SALA-01',
        owner: 'Juan Pérez',
        os: 'Windows 11 Pro',
        ip: '192.168.1.101',
        location: 'Oficina Principal - Piso 2',
        lastConnection: 'Hace 1 hora(s)',
        online: true,
        deviceType: 'pc',
      },
      {
        id: '1',
        name: 'PC-SALA-01',
        owner: 'Juan Pérez',
        os: 'Windows 11 Pro',
        ip: '192.168.1.101',
        location: 'Oficina Principal - Piso 2',
        lastConnection: 'Hace 1 hora(s)',
        online: true,
        deviceType: 'laptop',
      },
      {
        id: '1',
        name: 'PC-SALA-01',
        owner: 'Juan Pérez',
        os: 'Windows 11 Pro',
        ip: '192.168.1.101',
        location: 'Oficina Principal - Piso 2',
        lastConnection: 'Hace 1 hora(s)',
        online: false,
        deviceType: 'laptop',
      },
      {
        id: '1',
        name: 'PC-SALA-01',
        owner: 'Juan Pérez',
        os: 'Windows 11 Pro',
        ip: '192.168.1.101',
        location: 'Oficina Principal - Piso 2',
        lastConnection: 'Hace 1 hora(s)',
        online: true,
        deviceType: 'pc',
      },
      {
        id: '1',
        name: 'PC-SALA-01',
        owner: 'Juan Pérez',
        os: 'Windows 11 Pro',
        ip: '192.168.1.101',
        location: 'Oficina Principal - Piso 2',
        lastConnection: 'Hace 1 hora(s)',
        online: false,
        deviceType: 'tablet',
      },
      {
        id: '1',
        name: 'PC-SALA-01',
        owner: 'Juan Pérez',
        os: 'Windows 11 Pro',
        ip: '192.168.1.101',
        location: 'Oficina Principal - Piso 2',
        lastConnection: 'Hace 1 hora(s)',
        online: false,
        deviceType: 'pc',
      },
    ]);
    return { filter, rows };
  },
});
</script>
