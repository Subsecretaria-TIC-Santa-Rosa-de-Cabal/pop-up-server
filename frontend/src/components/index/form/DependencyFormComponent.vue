<template>
  <q-form @submit.prevent="submit">
    <div class="q-col-gutter-md">
      <div>
        <q-input
          outlined
          dense
          v-model="mainStore.dependencyFormData.name"
          label="Nombre"
        ></q-input>
      </div>

      <div>
        <q-input
          outlined
          dense
          type="tel"
          :mask="'#'.repeat(2)"
          v-model="mainStore.dependencyFormData.deviceCount"
          label="Cantidad de Dispositivos"
        ></q-input>
      </div>

      <div><q-btn class="full-width" color="primary" label="Registrar dependencia"></q-btn></div>
    </div>
  </q-form>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useMainStore } from 'src/stores/main-store';

export default defineComponent({
  name: 'DependencyFormComponent',

  components: {
    //
  },

  setup() {
    const mainStore = useMainStore();

    const submit = () => {};

    return { mainStore, submit };
  },
});
</script>
