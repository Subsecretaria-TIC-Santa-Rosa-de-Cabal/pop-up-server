import { makeRequest } from '../makeRequest';
import type { IPopUp } from 'src/modules/interfaces/popUp';

export interface IPopupCreate {
  name: string;
  description: string;
  date: string | null;
  image_base64?: string | undefined;
  dependency_identifier?: string | null;
}

export const apiPopupCreatePost = async (
  dependencyData: IPopupCreate,
  imageBase64?: string,
): Promise<IPopUp> => {
  if (imageBase64) dependencyData.image_base64 = imageBase64;
  dependencyData.date = dependencyData.date ? dependencyData.date : null;
  return await makeRequest({
    url: `/api/popup/launch`,
    method: 'POST',
    bodyData: { ...dependencyData },
  });
};
