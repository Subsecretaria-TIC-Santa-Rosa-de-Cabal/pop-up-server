<template>
  <div class="q-col-gutter-md">
    <div>
      <q-input
        outlined
        dense
        v-model="mainStore.popupFormData.name"
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
      <q-file
        outlined
        dense
        v-model="mainStore.popupUploadFile"
        label="Imagen"
        hint="Máximo 2 MB"
        accept=".jpg, image/*"
        max-file-size="2097152"
        :rules="[(val) => !!val || 'Obligatorio']"
        @rejected="onRejected"
      >
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
        disable
      >
        <template v-slot:prepend>
          <q-icon name="event" class="cursor-pointer">
            <q-popup-proxy cover transition-show="scale" transition-hide="scale">
              <q-date
                v-model="mainStore.popupFormData.date"
                mask="YYYY-MM-DD HH:mm"
                :options="optionsFn"
                today-btn
              >
                <div class="row items-center justify-end">
                  <q-btn v-close-popup label="Cerrar" color="primary" flat />
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
                  <q-btn v-close-popup label="Cerrar" color="primary" flat />
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

    <div>
      <q-select
        outlined
        dense
        v-model="mainStore.deviceFormData.dependency_identifier"
        :options="[{ name: 'TODAS', identifier: null }, ...mainStore.dependencies]"
        option-label="name"
        option-value="identifier"
        map-options
        emit-value
        label="Dependencia"
        :rules="[(val) => (val !== undefined && val !== '') || 'Selección obligatoria']"
      />
    </div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';
import { useMainStore } from 'src/stores/main-store';
import { useQuasar } from 'quasar';

export default defineComponent({
  name: 'PopupFormComponent',

  components: {
    //
  },

  setup() {
    const $q = useQuasar();
    const mainStore = useMainStore();

    const sendAllDependencies = ref(false);

    const getDependencies = async () => {
      await mainStore.getDependencies();
    };
    if (!mainStore.dependencies.length) void getDependencies();

    if (!mainStore.popupFormData.date)
      mainStore.popupFormData.date = new Date().toISOString().slice(0, 16).replace('T', ' ');

    const optionsFn = (date: string) => {
      // Comentario: Genera la fecha de hoy en formato 'YYYY/MM/DD' para comparación.
      const today = new Date().toISOString().slice(0, 10).replace(/-/g, '/');
      // Comentario: Retorna verdadero si la fecha (YYYY/MM/DD) es igual o posterior a hoy.
      return date >= today;
    };

    return {
      mainStore,
      sendAllDependencies,
      optionsFn,
      onRejected(rejectedEntries: { file: File; failedPropValidation: string }[]) {
        // Notify plugin needs to be installed
        // https://v2.quasar.dev/quasar-plugins/notify#Installation
        $q.notify({
          type: 'negative',
          message: `${rejectedEntries.length} archivo rechazado(s). Tamaño máximo permitido: 2MB.`,
        });
      },
    };
  },
});
</script>
