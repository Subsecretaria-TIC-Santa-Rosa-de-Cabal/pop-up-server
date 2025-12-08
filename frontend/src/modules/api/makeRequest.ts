import { getApiHost } from './configHost';
import { getAccesToken } from './session';

export interface IApiError extends Error {
  error_code?: string;
  message: string;
  data?: null;
  status?: string;
}

type HttpMethod = 'GET' | 'POST' | 'PUT' | 'DELETE' | 'PATCH' | 'HEAD' | 'OPTIONS';

interface RequestOptions {
  url: string;
  method?: HttpMethod;
  accessToken?: string;
  // eslint-disable-next-line @typescript-eslint/no-redundant-type-constituents
  bodyData?: object | object[] | null;
  baseURL?: string;
}

export const makeRequest = async <T = unknown>({
  url,
  method = 'GET',
  accessToken = '',
  bodyData = null,
  baseURL = getApiHost(),
}: RequestOptions): Promise<T> => {
  if (!accessToken) {
    accessToken = getAccesToken() || '';
  }

  const headers: HeadersInit = {
    'Content-Type': 'application/json',
    Authorization: `Bearer ${accessToken}`,
  };

  const options: RequestInit = {
    method,
    headers,
    body: bodyData ? JSON.stringify(bodyData) : null,
  };

  try {
    const response = await fetch(`${baseURL}${url}`, options);
    const data = await response.json();

    if (!response.ok || data.detail) {
      const error: IApiError = new Error();
      error.error_code = String(data.detail.error_code) || 'UNKNOWN_ERROR';
      throw error;
    }

    return data as T;
  } catch (err) {
    const error: IApiError = err instanceof Error ? err : new Error('Error desconocido');
    throw error;
  }
};
