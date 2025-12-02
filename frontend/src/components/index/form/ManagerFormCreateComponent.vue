<template>
  <div class="q-ma-md" v-if="mainStore.tabPage == 'popups'">
    <div class="text-bold text-h6 q-mb-md">
      {{ mainStore.popupFormData.identifier ? 'Editar' : 'Crear' }} Pop-up
    </div>
    <q-form @submit.prevent="submitCreatePopup">
      <PopupFormComponent />
      <div class="q-mt-md row justify-between">
        <q-btn color="negative" label="cancelar" @click="false"></q-btn>
        <q-btn
          color="primary"
          :label="(mainStore.dependencyFormData.identifier ? 'Editar' : 'Registrar') + ' Popup'"
          type="submit"
        ></q-btn>
      </div>
    </q-form>
  </div>

  <div class="q-ma-md" v-else-if="mainStore.tabPage == 'dependencies'">
    <div class="text-bold text-h6 q-mb-md">
      {{ mainStore.dependencyFormData.identifier ? 'Editar' : 'Registrar' }} Dependencia
    </div>
    <q-form @submit.prevent="submitDependencyCreate">
      <DependencyFormComponent />
      <div class="q-mt-md row justify-between">
        <q-btn
          color="negative"
          label="cancelar"
          @click="mainStore.unsetEditDependencyFormData"
        ></q-btn>
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
    <div class="text-bold text-h6 q-mb-md">Registrar Dispositivo</div>
    <q-form @submit.prevent="submitDeviceCreate">
      <DeviceFormComponent />
      <div class="q-mt-md row justify-between">
        <q-btn color="negative" label="cancelar" @click="false"></q-btn>
        <q-btn
          color="primary"
          :label="
            (mainStore.dependencyFormData.identifier ? 'Editar' : 'Registrar') + ' dispositivo'
          "
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
import { apiDeviceCreatePost } from 'src/modules/api/device/apiDeviceCreatePost';
import { apiPopupCreatePost } from 'src/modules/api/popup/apiPopupCreatePost';

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
        await apiPopupCreatePost(mainStore.popupFormData);
        $q.notify({
          message: 'Dependencia registrada',
          type: 'positive',
        });
      } catch {
        $q.notify({
          message: 'Error al crear el Popup',
          type: 'negative',
        });
      }
    };

    const submitDependencyCreate = async () => {
      try {
        $q.loading.show();
        await mainStore.createDependency();
        $q.notify({
          message: 'Dependencia registrada',
          type: 'positive',
        });
      } catch {
        $q.notify({
          message: 'Error al registrar la dependencia',
          type: 'negative',
        });
      } finally {
        $q.loading.hide();
      }
    };

    const submitDeviceCreate = async () => {
      try {
        await apiDeviceCreatePost(mainStore.dependencyFormData);
      } catch {
        $q.notify({
          message: 'Error al registrar el dispositivo',
          type: 'negative',
        });
      }
    };

    return { mainStore, submitCreatePopup, submitDependencyCreate, submitDeviceCreate };
  },
});
</script>
