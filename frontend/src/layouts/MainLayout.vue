<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn flat dense round icon="menu" aria-label="Menu" @click="toggleLeftDrawer" />

        <q-toolbar-title> Lanzar POPUP </q-toolbar-title>

        <div>Quasar v{{ $q.version }}</div>
      </q-toolbar>
    </q-header>

    <q-drawer v-model="leftDrawerOpen" show-if-above bordered>
      <q-list>
        <q-item-label header> LOGO </q-item-label>

        <EssentialRouteComponent v-for="link in linksList" :key="link.title" v-bind="link" />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import type { EssentialRouteProps } from 'src/components/EssentialRouteComponent.vue';
import EssentialRouteComponent from 'components/EssentialRouteComponent.vue';

const linksList: EssentialRouteProps[] = [
  {
    title: 'Inicio',
    caption: 'Lanzar popup',
    icon: 'launch',
    routeName: 'IndexPage',
  },
];

export default defineComponent({
  name: 'MainLayout',

  components: {
    EssentialRouteComponent,
  },

  setup() {
    const leftDrawerOpen = ref(false);

    return {
      linksList,
      leftDrawerOpen,
      toggleLeftDrawer() {
        leftDrawerOpen.value = !leftDrawerOpen.value;
      },
    };
  },
});
</script>
