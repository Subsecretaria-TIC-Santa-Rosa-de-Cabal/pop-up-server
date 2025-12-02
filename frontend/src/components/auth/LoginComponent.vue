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
import { defineComponent, ref } from 'vue';
import { useRouter } from 'vue-router';

export default defineComponent({
  name: 'LoginComponent',

  setup() {
    const $router = useRouter();

    const hostInput = ref('');
    const username = ref('');
    const password = ref('');

    const getHost = () => {
      hostInput.value = localStorage.getItem('serverHost') || '';
    };
    getHost();

    const handlerLogin = () => {
      const currentHost = localStorage.getItem('serverHost') || '';

      if (currentHost === '') {
        alert('Por favor, configure el host del servidor antes de iniciar sesión.');
        return;
      }
      localStorage.setItem('acces-token', username.value);
      localStorage.setItem('serverHost', hostInput.value);
      void $router.push({ name: 'IndexPage' });
    };

    return { username, password, hostInput, handlerLogin };
  },
});
</script>
