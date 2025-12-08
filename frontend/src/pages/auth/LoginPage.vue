<template>
  <q-page padding>
    <LoginComponent />
  </q-page>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import LoginComponent from 'src/components/auth/LoginComponent.vue';

export default defineComponent({
  name: 'LoginPage',

  components: {
    LoginComponent,
  },

  setup() {
    return {};
  },
});
</script>
