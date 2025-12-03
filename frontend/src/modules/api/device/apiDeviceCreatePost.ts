import { makeRequest } from '../makeRequest';
import type { IDevice } from 'src/modules/interfaces/device';

export interface IDeviceCreate {
  identifier?: string;
  name: string;
  IP: string;
  port: number;
  dependency_identifier: string;
}

export const apiDeviceCreatePost = async (dependencyData: IDeviceCreate): Promise<IDevice> => {
  dependencyData.port = Number(dependencyData.port);
  return await makeRequest({
    url: `/api/device/`,
    method: 'POST',
    bodyData: { ...dependencyData },
  });
};
