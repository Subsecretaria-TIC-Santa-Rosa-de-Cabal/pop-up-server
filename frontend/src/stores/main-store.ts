import { defineStore, acceptHMRUpdate } from 'pinia';
import type { IDependency } from 'src/components/modules/interfaces/dependency';
import type { IDevice } from 'src/components/modules/interfaces/device';
import type { IPopUp } from 'src/components/modules/interfaces/popUp';

const popupUploadFile: File | null = null;

export const useMainStore = defineStore('mainStore', {
  state: () => ({
    popupList: [],
    popupFormData: {} as IPopUp,
    popupUploadFile,
    popupTargets: [] as string[],

    dependencies: [],
    dependencyFormData: {} as IDependency,

    devices: [],
    deviceFormData: {} as IDevice,

    tabPage: 'popups',
    showFormDrawer: false,
  }),

  // getters: {
  //   doubleCount: (state) => state.counter * 2,
  // },

  actions: {
    // increment() {
    //   this.counter++;
    // },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useMainStore, import.meta.hot));
}
