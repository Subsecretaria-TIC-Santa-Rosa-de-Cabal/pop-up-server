import { defineStore, acceptHMRUpdate } from 'pinia';
import {
  apiDependencyCreatePost,
  type IDependencyCreate,
} from 'src/modules/api/dependency/apiDependencyCreatePost';
import { apiDependencyDelete } from 'src/modules/api/dependency/apiDependencyDelete';
import { apiDependencyGet } from 'src/modules/api/dependency/apiDependencyGet';
import type { IPopupCreate } from 'src/modules/api/popup/apiPopupCreatePost';
import type { IDependency } from 'src/modules/interfaces/dependency';
import type { IDevice } from 'src/modules/interfaces/device';

const popupUploadFile: File | null = null;

export const useMainStore = defineStore('mainStore', {
  state: () => ({
    popupList: [],
    popupFormData: {} as IPopupCreate,
    popupUploadFile,
    popupTargets: [] as string[],

    dependencies: [] as IDependency[],
    dependencyFormData: {} as IDependencyCreate,

    devices: [],
    deviceFormData: {} as IDevice,

    tabPage: 'popups',
    showFormDrawer: false,
  }),

  // getters: {
  //   doubleCount: (state) => state.counter * 2,
  // },

  actions: {
    //#region Dependencias
    setEditDependencyFormData(dependencyData: IDependency) {
      this.dependencyFormData = dependencyData;
      this.showFormDrawer = true;
    },
    unsetEditDependencyFormData() {
      this.dependencyFormData = {} as IDependency;
    },
    async createDependency() {
      const res = await apiDependencyCreatePost(this.dependencyFormData);
      if (res) {
        this.dependencies.push(res);
        this.unsetEditDependencyFormData();
      }
    },
    async getDependencies() {
      this.dependencies = await apiDependencyGet();
    },
    async deleteDependency(dependencyId: string) {
      const res = await apiDependencyDelete(dependencyId);
      const index = this.dependencies.findIndex((dep) => dep.identifier === res.identifier);
      if (index !== -1) this.dependencies.splice(index, 1);
    },
    //#endregion

    // async getDependencies() {
    //   await apiDependencyGet();
    // },
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useMainStore, import.meta.hot));
}
