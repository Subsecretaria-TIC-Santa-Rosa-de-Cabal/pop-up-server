import { makeRequest } from '../makeRequest';

export interface IDeviceCreate {
  name: string;
}

export const apiGetImageByIdentifier = async (popupId: string): Promise<string> => {
  return await makeRequest({
    url: `/api/popup/images/${popupId}`,
    method: 'GET',
  });
};
