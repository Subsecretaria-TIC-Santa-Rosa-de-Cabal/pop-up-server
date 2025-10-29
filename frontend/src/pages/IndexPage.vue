<template>
  <q-page padding>
    <div class="row justify-center">
      <q-card flat bordered class="col-8">
        <!-- <q-card-section class="q-pb-none"> Formulario popup </q-card-section> -->
        <q-card-section class="q-gutter-y-lg">
          <q-input outlined v-model="formComponent.title" label="Título"></q-input>
          <q-input outlined v-model="formComponent.title" label="Descripción"></q-input>
          <q-file outlined v-model="formComponent.image" label="Imagen"></q-file>

          <q-btn label="Envíar" unelevated color="primary" class="full-width"></q-btn>
        </q-card-section>
      </q-card>
    </div>
  </q-page>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';

interface IFormPopup {
  title: string;
  description: string;
  image: File;
}
export default defineComponent({
  name: 'IndexPage',

  components: {
    //
  },

  setup() {
    const formComponent = ref<IFormPopup>({
      title: '',
      description: '',
      image: {} as File,
    });
    return { formComponent };
  },
});
</script>
