import { makeRequest } from '../makeRequest';
import type { IDevice } from 'src/modules/interfaces/device';

export const apiDeviceDelete = async (dependencyId: string): Promise<IDevice> => {
  return await makeRequest({
    url: `/api/device/` + dependencyId,
    method: 'DELETE',
  });
};
