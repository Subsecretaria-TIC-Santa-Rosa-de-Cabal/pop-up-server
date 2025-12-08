<template>
  <q-layout view="hHh lpR fFr">
    <q-header class="bg-white">
      <q-toolbar>
        <!-- <q-btn flat dense round icon="menu" aria-label="Menu" @click="toggleLeftDrawer" /> -->

        <!-- <q-icon color="primary" text-color="white" name="desktop_windows" size="md"></q-icon> -->
        <q-avatar square>
          <q-img :ratio="1" fit="contain" src="logos/logo_icon.png"></q-img>
        </q-avatar>
        <q-toolbar-title class="text-black"> Sistema de Pop-ups Corporativos</q-toolbar-title>

        <div class="q-mx-md text-black">
          <div class="text-bold">{{ 'Admin' }} ({{ 'Administrador' }})</div>
        </div>
        <q-btn color="negative" flat dense icon="refresh" @click="$router.go(0)" />
        <q-btn
          color="negative"
          flat
          dense
          icon="logout"
          aria-label="Logout"
          @click="confirmLogout"
        />
      </q-toolbar>
      <q-separator></q-separator>
    </q-header>

    <q-drawer
      :width="400"
      :breakpoint="1200"
      show-if-above
      v-model="mainStore.showFormDrawer"
      side="right"
      bordered
    >
      <ManagerFormCreateComponent />
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

import { useRouter } from 'vue-router';
import { getAccesToken, removeSessionStorage } from 'src/modules/api/session';

import ManagerFormCreateComponent from 'src/components/index/form/ManagerFormCreateComponent.vue';
import { useQuasar } from 'quasar';

export default defineComponent({
  name: 'MainLayout',

  components: {
    ManagerFormCreateComponent,
  },

  setup() {
    const $q = useQuasar();
    const $router = useRouter();
    const mainStore = useMainStore();

    const leftDrawerOpen = ref(false);
    const rightDrawerOpen = ref(false);

    const guard = () => {
      if (getAccesToken()) return;
      logout();
    };

    const logout = () => {
      removeSessionStorage();
      void $router.push({ name: 'LoginPage' });
    };

    const confirmLogout = () => {
      $q.dialog({
        title: '¿Cerrar sesión?',
        // message: 'Would you like to turn on the wifi?',
        cancel: true,
        persistent: false,
      }).onOk(() => {
        logout();
      });
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

      confirmLogout,
    };
  },
});
</script>
