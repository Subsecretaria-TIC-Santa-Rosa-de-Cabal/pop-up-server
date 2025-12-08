import type { IAuthResponse } from 'src/modules/interfaces/authResponse';
import { makeRequest } from '../makeRequest';

export const apiLoginPost = async (
  username: string,
  password: string,
  hosting: string,
): Promise<IAuthResponse> => {
  return await makeRequest({
    url: `/api/auth/login`,
    method: 'POST',
    bodyData: { username, password },
    baseURL: hosting,
  });
};
