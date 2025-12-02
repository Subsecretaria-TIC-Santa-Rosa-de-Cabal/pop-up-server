<template>
  <div>
    <div class="column items-center q-mb-xl">
      <div class="q-mb-md">
        <q-avatar color="primary" text-color="white" icon="desktop_windows" size="xl" />
      </div>
      <div class="text-bold">Sistema de Pop-ups Corporativos</div>
      <div>Gestión centralizada de notificaciones empresariales</div>
    </div>
    <q-card style="width: 400px">
      <q-card-section>
        <div class="text-bold text-h6">Iniciar sesión</div>
        <div class="text-grey">
          Ingresa tus credenciales para acceder al panel de administración
        </div>
      </q-card-section>

      <q-form @submit.prevent="handlerLogin">
        <q-card-section>
          <div>
            <div>Host</div>
            <q-input
              outlined
              dense
              v-model="hostInput"
              @blur="hostInput = hostInput.replace(/\/$/, '')"
              :rules="[(val) => !!val || 'Obligatorio']"
            />
          </div>

          <div>
            <div>Usuario</div>
            <q-input outlined dense v-model="username" :rules="[(val) => !!val || 'Obligatorio']" />
          </div>

          <div>
            <div>Password</div>
            <q-input
              outlined
              dense
              type="password"
              v-model="password"
              :rules="[(val) => !!val || 'Obligatorio']"
            />
          </div>

          <q-btn
            unelevated
            color="primary"
            label="Iniciar sesión"
            class="full-width"
            type="submit"
          ></q-btn>
        </q-card-section>
      </q-form>
    </q-card>
  </div>
</template>

<script lang="ts">
import { useQuasar } from 'quasar';

import { apiLoginPost } from 'src/modules/api/auth/login';
import { getApiHost, setApiHost } from 'src/modules/api/configHost';
import type { IApiError } from 'src/modules/api/makeRequest';
import { setSessionStorage } from 'src/modules/api/session';
import { translateErrorCodeToMessage } from 'src/modules/api/translateErrorCodeToMessage';
import { defineComponent, ref } from 'vue';
import { useRouter } from 'vue-router';

export default defineComponent({
  name: 'LoginComponent',

  setup() {
    const $q = useQuasar();
    const $router = useRouter();

    const hostInput = ref(getApiHost() || '');
    const username = ref('');
    const password = ref('');

    const handlerLogin = async () => {
      if (hostInput.value === '') {
        alert('Por favor, configure el host del servidor antes de iniciar sesión.');
        return;
      }

      try {
        const authResponse = await apiLoginPost(username.value, password.value, hostInput.value);

        setSessionStorage(authResponse);
        setApiHost(hostInput.value);

        $q.notify({
          message: 'Inició sesión',
          type: 'positive',
        });

        setTimeout(() => {
          void $router.push({ name: 'IndexPage' });
        }, 100);
      } catch (error) {
        const codeError = (error as IApiError).error_code;
        $q.notify({
          message: translateErrorCodeToMessage(codeError) || 'Error desconocido o de conexión',
          type: 'negative',
        });
      }
    };

    return { username, password, hostInput, handlerLogin };
  },
});
</script>
