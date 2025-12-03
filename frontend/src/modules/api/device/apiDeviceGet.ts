import { makeRequest } from '../makeRequest';
import type { IDevice } from 'src/modules/interfaces/device';

export interface IDeviceCreate {
  name: string;
}

export const apiDeviceGet = async (): Promise<IDevice[]> => {
  return await makeRequest({
    url: `/api/device/`,
    method: 'GET',
  });
};
