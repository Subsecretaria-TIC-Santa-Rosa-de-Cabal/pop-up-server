<template>
  <q-layout view="hHh lpR fFr">
    <q-header class="bg-white">
      <q-toolbar>
        <!-- <q-btn flat dense round icon="menu" aria-label="Menu" @click="toggleLeftDrawer" /> -->

        <q-icon color="primary" text-color="white" name="desktop_windows" size="md"></q-icon>
        <q-toolbar-title class="text-black"> Sistema de Pop-ups Corporativos</q-toolbar-title>

        <div class="q-mx-md text-black">
          <div class="text-bold">{{ 'Admin' }} ({{ 'Administrador' }})</div>
        </div>
        <q-btn color="negative" flat dense icon="refresh" @click="$router.go(0)" />
        <q-btn color="negative" flat dense icon="logout" aria-label="Logout" @click="logout" />
      </q-toolbar>
      <q-separator></q-separator>
    </q-header>

    <q-drawer show-if-above v-model="mainStore.showFormDrawer" side="right" bordered>
      <div class="q-ma-md" v-if="mainStore.tabPage == 'popups'">
        <div class="text-bold text-h6 q-mb-md">Crear Pop-up</div>
        <PopupFormComponent />
      </div>
      <div class="q-ma-md" v-else-if="mainStore.tabPage == 'dependencies'">
        <div class="text-bold text-h6 q-mb-md">Registrar Dependencia</div>
        <DependencyFormComponent />
      </div>
      <div class="q-ma-md" v-else-if="mainStore.tabPage == 'devices'">
        <div class="text-bold text-h6 q-mb-md">Registrar Dispositivo</div>
        <DeviceFormComponent />
      </div>
    </q-drawer>

    <q-page-container>
      <div class="bg-blue-grey-1 absolute-full"></div>
      <router-view />

      <!-- <q-page-sticky position="bottom-right" :offset="[18, 18]">
        <q-btn color="accent" label="Nuevo Pop-up" icon="add" />
      </q-page-sticky> -->
    </q-page-container>
  </q-layout>
</template>

<script lang="ts">
import { defineComponent, onMounted, ref } from 'vue';

import { useMainStore } from 'src/stores/main-store';
import PopupFormComponent from 'src/components/index/form/PopupFormComponent.vue';
import DependencyFormComponent from 'src/components/index/form/DependencyFormComponent.vue';
import DeviceFormComponent from 'src/components/index/form/DeviceFormComponent.vue';
import { useRouter } from 'vue-router';

export default defineComponent({
  name: 'MainLayout',

  components: {
    PopupFormComponent,
    DependencyFormComponent,
    DeviceFormComponent,
  },

  setup() {
    const $router = useRouter();
    const mainStore = useMainStore();

    const leftDrawerOpen = ref(false);
    const rightDrawerOpen = ref(false);

    const guard = () => {
      if (localStorage.getItem('acces-token')) return;
      logout();
    };

    const logout = () => {
      localStorage.removeItem('acces-token');
      void $router.push({ name: 'LoginPage' });
    };

    onMounted(() => {
      guard();
    });

    return {
      mainStore,
      leftDrawerOpen,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value;
      },
      rightDrawerOpen,
      logout,
    };
  },
});
</script>
