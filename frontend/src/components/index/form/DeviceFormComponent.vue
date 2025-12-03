<template>
  <div class="q-col-gutter-md">
    <div>
      <q-input
        outlined
        dense
        v-model="mainStore.deviceFormData.name"
        label="Nombre"
        :rules="[(val) => !!val || 'Obligatorio']"
      ></q-input>
    </div>

    <div>
      <q-input
        outlined
        dense
        v-model="mainStore.deviceFormData.IP"
        label="IP"
        :rules="[(val) => !!val || 'Obligatorio']"
        :disable="!!mainStore.deviceFormData.identifier"
      ></q-input>
    </div>

    <div>
      <q-input
        outlined
        dense
        v-model="mainStore.deviceFormData.port"
        label="Puerto"
        type="tel"
        mask="##########"
        :rules="[(val) => !!val || 'Obligatorio']"
        :disable="!!mainStore.deviceFormData.identifier"
      ></q-input>
    </div>

    <div>
      <q-select
        outlined
        dense
        v-model="mainStore.deviceFormData.dependency_identifier"
        :options="mainStore.dependencies"
        option-label="name"
        option-value="identifier"
        map-options
        emit-value
        label="Dependencia"
        :rules="[(val) => !!val || 'Obligatorio']"
      />
    </div>
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

    const getDependencies = async () => {
      await mainStore.getDependencies();
    };
    if (!mainStore.dependencies.length) void getDependencies();

    return { mainStore, getDependencies };
  },
});
</script>
