import { makeRequest } from '../makeRequest';
import type { IDependency } from 'src/modules/interfaces/dependency';

export const apiDependencyGet = async (): Promise<IDependency[]> => {
  return await makeRequest({
    url: `/api/dependency/`,
    method: 'GET',
  });
};
