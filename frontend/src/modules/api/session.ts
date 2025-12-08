import type { IAuthResponse } from '../interfaces/authResponse';

export const setSessionStorage = (authResponse: IAuthResponse) => {
  localStorage.setItem('user_role', JSON.stringify(authResponse.role));
  localStorage.setItem('access_token', authResponse.access_token);
  localStorage.setItem('access_token', authResponse.access_token);
};

export const removeSessionStorage = () => {
  localStorage.removeItem('user_role');
  localStorage.removeItem('access_token');
  localStorage.removeItem('access_token');
};

export const getUserRole = () => JSON.parse(localStorage.getItem('user_role') || '') || null;
export const getUserData = () => JSON.parse(localStorage.getItem('access_token') || '') || null;
export const getAccesToken = () => localStorage.getItem('access_token') || '';

export const getSessionStorage = (): IAuthResponse => {
  const authResponse = {} as IAuthResponse;
  authResponse.role = getUserRole();
  authResponse.user = getUserData();
  authResponse.access_token = getAccesToken();

  return authResponse;
};
