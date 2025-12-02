import { makeRequest } from '../makeRequest';
import type { IDevice } from 'src/modules/interfaces/device';

export interface IDeviceCreate {
  name: string;
}

export const apiDeviceCreatePost = async (dependencyData: IDeviceCreate): Promise<IDevice> => {
  return await makeRequest({
    url: `/api/device/`,
    method: 'POST',
    bodyData: { dependencyData },
  });
};
