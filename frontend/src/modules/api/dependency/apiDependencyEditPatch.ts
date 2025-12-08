import { makeRequest } from '../makeRequest';
import type { IDependency } from 'src/modules/interfaces/dependency';

export interface IDependencyEdit {
  name: string;
}

export const apiDependencyEditPatch = async (
  dependencyData: IDependencyEdit,
): Promise<IDependency> => {
  return await makeRequest({
    url: `/api/dependency/`,
    method: 'PATCH',
    bodyData: { ...dependencyData },
  });
};
