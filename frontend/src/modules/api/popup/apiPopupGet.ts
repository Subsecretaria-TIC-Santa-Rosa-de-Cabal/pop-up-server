import { makeRequest } from '../makeRequest';
import type { IPopUp } from 'src/modules/interfaces/popUp';

export const apiPopupGet = async (): Promise<IPopUp[]> => {
  return await makeRequest({
    url: `/api/popup/`,
    method: 'GET',
  });
};
