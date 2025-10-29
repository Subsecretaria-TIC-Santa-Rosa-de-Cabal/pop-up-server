<template>
  <q-item clickable :to="{ name: routeName }" :active="$route.name == routeName">
    <q-item-section v-if="icon" avatar>
      <q-icon :name="icon" />
    </q-item-section>

    <q-item-section>
      <q-item-label>{{ title }}</q-item-label>
      <q-item-label caption>{{ caption }}</q-item-label>
    </q-item-section>
  </q-item>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export interface EssentialRouteProps {
  title: string;
  caption?: string;
  routeName?: string;
  icon?: string;
}

export default defineComponent({
  name: 'EssentialRouteComponent',
  props: {
    title: {
      type: String,
      required: true,
    },

    caption: {
      type: String,
      default: '',
    },

    routeName: {
      type: String,
      default: '#',
    },

    icon: {
      type: String,
      default: '',
    },
  },
});
</script>
