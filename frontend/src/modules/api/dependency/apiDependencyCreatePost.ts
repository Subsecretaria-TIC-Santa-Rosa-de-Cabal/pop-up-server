import { makeRequest } from '../makeRequest';
import type { IDependency } from 'src/modules/interfaces/dependency';

export interface IDependencyCreate {
  identifier?: string;
  name: string;
}

export const apiDependencyCreatePost = async (
  dependencyData: IDependencyCreate,
): Promise<IDependency> => {
  return await makeRequest({
    url: `/api/dependency/`,
    method: 'POST',
    bodyData: { ...dependencyData },
  });
};
