import { defineStore, acceptHMRUpdate } from 'pinia';
import {
  apiDependencyCreatePost,
  type IDependencyCreate,
} from 'src/modules/api/dependency/apiDependencyCreatePost';
import type { IDeviceCreate } from 'src/modules/api/device/apiDeviceCreatePost';
import type { IPopupCreate } from 'src/modules/api/popup/apiPopupCreatePost';
import type { IDependency } from 'src/modules/interfaces/dependency';
import type { IDevice } from 'src/modules/interfaces/device';

import { apiDependencyDelete } from 'src/modules/api/dependency/apiDependencyDelete';
import { apiDependencyEditPatch } from 'src/modules/api/dependency/apiDependencyEditPatch';
import { apiDependencyGet } from 'src/modules/api/dependency/apiDependencyGet';
import { apiDeviceCreatePost } from 'src/modules/api/device/apiDeviceCreatePost';
import { apiDeviceEditPatch } from 'src/modules/api/device/apiDeviceEditPatch';
import { apiDeviceGet } from 'src/modules/api/device/apiDeviceGet';
import { apiDeviceDelete } from 'src/modules/api/device/apiDeviceDelete';

const popupUploadFile: File | null = null;

export const useMainStore = defineStore('mainStore', {
  state: () => ({
    popupList: [],
    popupFormData: {} as IPopupCreate,
    popupUploadFile,
    popupTargets: [] as string[],

    dependencies: [] as IDependency[],
    dependencyFormData: {} as IDependencyCreate,

    devices: [] as IDevice[],
    deviceFormData: {} as IDeviceCreate,

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
    unsetDependencyFormData() {
      this.dependencyFormData = {} as IDependency;
    },
    async createDependency() {
      const res = await apiDependencyCreatePost(this.dependencyFormData);
      if (res) {
        this.dependencies.push(res);
        this.unsetDependencyFormData();
      }
    },
    async editDependency() {
      const res = await apiDependencyEditPatch(this.dependencyFormData);
      if (res) {
        this.dependencies = this.dependencies.map((anyDependency) => {
          if (anyDependency.identifier == res.identifier) anyDependency = res;
          return anyDependency;
        });
        this.unsetDependencyFormData();
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

    //#region Dispositivos
    setEditDeviceFormData(deviceData: IDevice) {
      this.deviceFormData = deviceData;
      this.showFormDrawer = true;
    },
    unsetDeviceFormData() {
      this.deviceFormData = {} as IDevice;
    },
    async createDevice() {
      const res = await apiDeviceCreatePost(this.deviceFormData);
      if (res) {
        this.devices.push(res);
        this.unsetDeviceFormData();
      }
    },
    async editDevice() {
      const res = await apiDeviceEditPatch(this.deviceFormData);
      if (res) {
        this.devices = this.devices.map((anyDevice) => {
          if (anyDevice.identifier == res.identifier) anyDevice = res;
          return anyDevice;
        });
        this.unsetDeviceFormData();
      }
    },
    async getDevices() {
      this.devices = await apiDeviceGet();
    },
    async deleteDevice(deviceId: string) {
      const res = await apiDeviceDelete(deviceId);
      const index = this.devices.findIndex((dep) => dep.identifier === res.identifier);
      if (index !== -1) this.devices.splice(index, 1);
    },
    //#endregion
  },
});

if (import.meta.hot) {
  import.meta.hot.accept(acceptHMRUpdate(useMainStore, import.meta.hot));
}
