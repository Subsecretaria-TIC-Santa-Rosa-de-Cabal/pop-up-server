<template>
  <q-layout view="lHh Lpr lFf">
    <q-page-container>
      <router-view />
      <!--
      <q-page-sticky position="top-right" :offset="[18, 18]">
        <q-btn color="accent" icon="wifi" label="Cambiar host" @click="showHostDialog = true" />
        <div class="text-grey row justify-center">IP: {{ currentHost || 'SIN REGISTRAR' }}</div>
      </q-page-sticky> -->
    </q-page-container>
  </q-layout>

  <q-dialog v-model="showHostDialog">
    <q-card>
      <q-card-section>
        <div class="text-h6">Configurar Host del Servidor</div>
      </q-card-section>

      <q-form @submit.prevent="setServerHost">
        <q-card-section>
          <q-input outlined label="Host del Servidor" v-model="hostInput" />
        </q-card-section>

        <q-card-actions align="right">
          <q-btn flat label="Cancelar" color="primary" v-close-popup />
          <q-btn flat label="Guardar" color="primary" type="submit" />
        </q-card-actions>
      </q-form>
    </q-card>
  </q-dialog>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';

export default defineComponent({
  name: 'AuthLayout',

  components: {
    //
  },

  setup() {
    const currentHost = ref('');
    const hostInput = ref('');
    const showHostDialog = ref(false);

    const getHost = () => {
      currentHost.value = localStorage.getItem('server-host') || '';
      hostInput.value = currentHost.value;
    };
    getHost();

    const setServerHost = () => {
      localStorage.setItem('server-host', hostInput.value);
      currentHost.value = hostInput.value;
      showHostDialog.value = false;
    };

    return { currentHost, hostInput, showHostDialog, setServerHost };
  },
});
</script>
