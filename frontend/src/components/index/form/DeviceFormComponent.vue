<template>
  <div class="q-col-gutter-md">
    <div>
      <q-input outlined dense v-model="mainStore.deviceFormData.name" label="Nombre"></q-input>
    </div>

    <div>
      <q-input outlined dense v-model="mainStore.deviceFormData.ip" label="IP"></q-input>
    </div>

    <div>
      <q-select
        outlined
        dense
        v-model="mainStore.popupTargets"
        multiple
        :options="['1', '2']"
        use-chips
        stack-label
        label="Dependencia"
      />
    </div>

    <div><q-btn class="full-width" color="primary" label="Registrar Dispositivo"></q-btn></div>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useMainStore } from 'src/stores/main-store';

export default defineComponent({
  name: 'DeviceFormComponent',

  components: {
    //
  },

  setup() {
    const mainStore = useMainStore();

    return { mainStore };
  },
});
</script>
