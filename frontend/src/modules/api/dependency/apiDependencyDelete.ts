import { makeRequest } from '../makeRequest';
import type { IDependency } from 'src/modules/interfaces/dependency';

export const apiDependencyDelete = async (dependencyId: string): Promise<IDependency> => {
  return await makeRequest({
    url: `/api/dependency/` + dependencyId,
    method: 'DELETE',
  });
};
