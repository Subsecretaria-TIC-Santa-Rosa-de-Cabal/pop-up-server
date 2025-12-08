import type { IDevice } from 'src/modules/interfaces/device';
import { makeRequest } from '../makeRequest';
import type { IDeviceCreate } from './apiDeviceCreatePost';

export const apiDeviceEditPatch = async (dependencyData: IDeviceCreate): Promise<IDevice> => {
  return await makeRequest({
    url: `/api/device/`,
    method: 'PATCH',
    bodyData: { ...dependencyData },
  });
};
