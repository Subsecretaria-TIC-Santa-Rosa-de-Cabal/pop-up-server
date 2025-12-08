import { makeRequest } from '../makeRequest';
import type { IPopUp } from 'src/modules/interfaces/popUp';

export interface IPopupCreate {
  identifier?: string;
  title: string;
  description: string;
  date: string;
  imageUrl?: '';
  targets: string[];
}

export const apiPopupCreatePost = async (dependencyData: IPopupCreate): Promise<IPopUp> => {
  return await makeRequest({
    url: `/api/ASDASDASDASDADASDASDASD/`,
    method: 'POST',
    bodyData: { dependencyData },
  });
};
