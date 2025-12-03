export interface IDevice {
  identifier?: string;
  enabled: boolean;
  registration_date: string;
  last_update: string;
  dependency_identifier: string;
  name: string;
  status: string;
  IP: string;
  port: number;
  last_connection: string;
  hostname: string;
  mac: string;
  operating_system: string;
}
