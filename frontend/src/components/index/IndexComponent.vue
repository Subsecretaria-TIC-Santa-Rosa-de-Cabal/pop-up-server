<template>
  <!-- PÁGINAS -->
  <div class="row justify-between items-center q-mb-md">
    <q-btn-toggle
      v-model="mainStore.tabPage"
      no-caps
      rounded
      unelevated
      toggle-color="primary"
      color="white"
      text-color="primary"
      :options="[
        { label: 'Pop-ups', value: 'popups' },
        { label: 'Dependencias', value: 'dependencies' },
        { label: 'Dispositivos', value: 'devices' },
      ]"
    />

    <q-btn
      round
      unelevated
      color="primary"
      :icon="mainStore.showFormDrawer ? 'remove' : 'add'"
      @click="mainStore.showFormDrawer = !mainStore.showFormDrawer"
    ></q-btn>
  </div>

  <div v-if="mainStore.tabPage == 'popups'">
    <div class="row justify-between items-center q-mb-md">
      <div
        v-for="{ id, title, count, icon, iconColor } in cardInformation"
        :key="id"
        class="col-xs-12 col-sm-4 q-gutter-md"
      >
        <q-card flat bordered>
          <q-item>
            <q-item-section>
              <q-item-label class="text-grey text-h6">{{ title }}</q-item-label>
              <q-item-label class="text-h4 text-bold">{{ count }} </q-item-label>
            </q-item-section>
            <q-item-section avatar>
              <q-icon :color="iconColor" :name="icon" size="xl" />
            </q-item-section>
          </q-item>
        </q-card>
      </div>
    </div>

    <q-separator></q-separator>

    <PopupTableComponent />
  </div>
  <div v-else-if="mainStore.tabPage == 'dependencies'">
    <div class="row justify-between items-center q-mb-md">
      <div
        v-for="{ id, title, count, icon, iconColor } in cardDevicesInformation"
        :key="id"
        class="col-xs-12 col-sm-4 q-gutter-md"
      >
        <q-card flat bordered>
          <q-item>
            <q-item-section>
              <q-item-label class="text-grey text-h6">{{ title }}</q-item-label>
              <q-item-label class="text-h4 text-bold">{{ count }} </q-item-label>
            </q-item-section>
            <q-item-section avatar>
              <q-icon :color="iconColor" :name="icon" size="xl" />
            </q-item-section>
          </q-item>
        </q-card>
      </div>
    </div>

    <q-separator></q-separator>

    <DependencyTableComponent />
  </div>

  <div v-else-if="mainStore.tabPage == 'devices'">
    <div class="row justify-between items-center q-mb-md">
      <div
        v-for="{ id, title, count, icon, iconColor } in cardDevicesInformation"
        :key="id"
        class="col-xs-12 col-sm-4 q-gutter-md"
      >
        <q-card flat bordered>
          <q-item>
            <q-item-section>
              <q-item-label class="text-grey text-h6">{{ title }}</q-item-label>
              <q-item-label class="text-h4 text-bold">{{ count }} </q-item-label>
            </q-item-section>
            <q-item-section avatar>
              <q-icon :color="iconColor" :name="icon" size="xl" />
            </q-item-section>
          </q-item>
        </q-card>
      </div>
    </div>

    <q-separator></q-separator>

    <DevicesTableComponent />
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';

import { useMainStore } from 'src/stores/main-store';

import PopupTableComponent from './PopupTableComponent.vue';
import DevicesTableComponent from './DevicesTableComponent.vue';
import DependencyTableComponent from './DependencyTableComponent.vue';

export default defineComponent({
  name: 'IndexComponent',

  components: {
    PopupTableComponent,
    DependencyTableComponent,
    DevicesTableComponent,
  },

  setup() {
    const mainStore = useMainStore();

    const searchFilter = ref('');
    const cardInformation = ref([
      { id: '1', title: 'Programados', count: 2, icon: 'event', iconColor: 'primary' },
      { id: '2', title: 'Activos', count: 5, icon: 'notifications', iconColor: 'positive' },
      { id: '3', title: 'Completados', count: 3, icon: 'check_circle', iconColor: 'grey' },
    ]);

    const cardDevicesInformation = ref([
      { id: '1', title: 'Dispositivos', count: 20, icon: 'tv', iconColor: 'primary' },
      { id: '2', title: 'En Línea', count: 15, icon: 'wifi', iconColor: 'positive' },
      { id: '3', title: 'Fuera de Línea', count: 5, icon: 'wifi_off', iconColor: 'grey' },
    ]);

    return { cardInformation, cardDevicesInformation, mainStore, searchFilter };
  },
});
</script>
