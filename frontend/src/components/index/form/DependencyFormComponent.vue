<template>
  <div class="q-col-gutter-md">
    <div>
      <q-input
        outlined
        dense
        v-model="mainStore.dependencyFormData.name"
        label="Nombre"
        :rules="[(val) => !!val || 'Obligatorio']"
      ></q-input>
    </div>
  </div>
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

    return { mainStore };
  },
});
</script>
