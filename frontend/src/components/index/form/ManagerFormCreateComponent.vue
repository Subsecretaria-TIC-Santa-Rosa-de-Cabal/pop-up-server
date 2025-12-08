<template>
  <div class="q-ma-md" v-if="mainStore.tabPage == 'popups'">
    <div class="text-bold text-h6 q-mb-md">
      <!-- {{ mainStore.popupFormData ? 'Editar' : 'Crear' }} Pop-up -->
      Lanazar Pop-up
    </div>
    <q-form @submit.prevent="submitCreatePopup">
      <PopupFormComponent />
      <div class="q-mt-md row justify-between">
        <q-btn color="negative" label="cancelar" @click="false"></q-btn>
        <q-btn
          color="primary"
          :label="(mainStore.dependencyFormData.identifier ? 'Editar' : 'Lanzar') + ' Popup'"
          type="submit"
        ></q-btn>
      </div>
    </q-form>
  </div>

  <div class="q-ma-md" v-else-if="mainStore.tabPage == 'dependencies'">
    <div class="text-bold text-h6 q-mb-md">
      {{ mainStore.dependencyFormData.identifier ? 'Editar' : 'Registrar' }} Dependencia
    </div>
    <q-form @submit.prevent="submitDependency">
      <DependencyFormComponent />
      <div class="q-mt-md row justify-between">
        <q-btn color="negative" label="cancelar" @click="mainStore.unsetDependencyFormData"></q-btn>
        <q-btn
          color="primary"
          :label="
            (mainStore.dependencyFormData.identifier ? 'Editar' : 'Registrar') + ' dependencia'
          "
          type="submit"
        ></q-btn>
      </div>
    </q-form>
  </div>

  <div class="q-ma-md" v-else-if="mainStore.tabPage == 'devices'">
    <div class="text-bold text-h6 q-mb-md">
      {{ mainStore.deviceFormData.identifier ? 'Editar' : 'Registrar' }} Dispositivo
    </div>
    <q-form @submit.prevent="submitDevice">
      <DeviceFormComponent />
      <div class="q-mt-md row justify-between">
        <q-btn color="negative" label="cancelar" @click="mainStore.unsetDeviceFormData"></q-btn>
        <q-btn
          color="primary"
          :label="(mainStore.deviceFormData.identifier ? 'Editar' : 'Registrar') + ' dispositivo'"
          type="submit"
        ></q-btn>
      </div>
    </q-form>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useMainStore } from 'src/stores/main-store';

import PopupFormComponent from './PopupFormComponent.vue';
import DependencyFormComponent from './DependencyFormComponent.vue';
import DeviceFormComponent from './DeviceFormComponent.vue';

import { useQuasar } from 'quasar';

export default defineComponent({
  name: 'ManagerFormCreateComponent',

  components: {
    PopupFormComponent,
    DependencyFormComponent,
    DeviceFormComponent,
  },

  setup() {
    const $q = useQuasar();
    const mainStore = useMainStore();

    const submitCreatePopup = async () => {
      try {
        await mainStore.createPopUp();
        $q.notify({
          message: 'Completado',
          type: 'positive',
        });
      } catch {
        $q.notify({
          message: 'Error',
          type: 'negative',
        });
      }
    };

    const submitDependency = async () => {
      try {
        $q.loading.show();
        if (mainStore.dependencyFormData.identifier) await mainStore.editDependency();
        else await mainStore.createDependency();
        $q.notify({
          message: 'Completado',
          type: 'positive',
        });
      } catch {
        $q.notify({
          message: 'Error',
          type: 'negative',
        });
      } finally {
        $q.loading.hide();
      }
    };

    const submitDevice = async () => {
      try {
        if (mainStore.deviceFormData.identifier) await mainStore.editDevice();
        else await mainStore.createDevice();
        $q.notify({
          message: 'Completado',
          type: 'positive',
        });
      } catch {
        $q.notify({
          message: 'Error',
          type: 'negative',
        });
      }
    };

    return { mainStore, submitCreatePopup, submitDependency, submitDevice };
  },
});
</script>
