<template>
  <div class="q-col-gutter-md">
    <div>
      <q-input
        outlined
        dense
        v-model="mainStore.popupFormData.title"
        label="Título"
        :rules="[(val) => !!val || 'Obligatorio']"
      ></q-input>
    </div>

    <div>
      <q-input
        outlined
        dense
        v-model="mainStore.popupFormData.description"
        label="Descripción"
        :rules="[(val) => !!val || 'Obligatorio']"
      ></q-input>
    </div>

    <div>
      <q-file outlined dense v-model="mainStore.popupUploadFile" label="Imagen (opcional)">
        <template v-slot:prepend>
          <q-icon name="attach_file" />
        </template>
      </q-file>
    </div>

    <div>
      <q-input
        outlined
        dense
        v-model="mainStore.popupFormData.date"
        :rules="[(val) => !!val || 'Obligatorio']"
      >
        <template v-slot:prepend>
          <q-icon name="event" class="cursor-pointer">
            <q-popup-proxy cover transition-show="scale" transition-hide="scale">
              <q-date v-model="mainStore.popupFormData.date" mask="YYYY-MM-DD HH:mm">
                <div class="row items-center justify-end">
                  <q-btn v-close-popup label="Close" color="primary" flat />
                </div>
              </q-date>
            </q-popup-proxy>
          </q-icon>
        </template>

        <template v-slot:append>
          <q-icon name="access_time" class="cursor-pointer">
            <q-popup-proxy cover transition-show="scale" transition-hide="scale">
              <q-time v-model="mainStore.popupFormData.date" mask="YYYY-MM-DD HH:mm" format24h>
                <div class="row items-center justify-end">
                  <q-btn v-close-popup label="Close" color="primary" flat />
                </div>
              </q-time>
            </q-popup-proxy>
          </q-icon>
        </template>
      </q-input>
    </div>

    <div>
      <q-separator></q-separator>
    </div>

    <div class="text-bold text-h6">Dispositivos</div>
    <!-- <q-toggle v-model="selectAllDevices" label="Todos los dispositivos"></q-toggle> -->
    <q-select
      outlined
      dense
      v-model="mainStore.popupTargets"
      multiple
      :options="['1', '2']"
      use-chips
      stack-label
      label="Dispositivos Destino"
      :rules="[(val) => !!val || 'Obligatorio']"
    />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { useMainStore } from 'src/stores/main-store';

export default defineComponent({
  name: 'PopupFormComponent',

  components: {
    //
  },

  setup() {
    const mainStore = useMainStore();

    return { mainStore };
  },
});
</script>
