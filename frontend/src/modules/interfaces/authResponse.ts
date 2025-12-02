import type { IRole } from './role';
import type { IUser } from './user';

export interface IAuthResponse {
  role: IRole | null;
  user: IUser | null;
  access_token: string;
}
