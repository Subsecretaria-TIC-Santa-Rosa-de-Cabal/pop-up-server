export const getApiHost = () => localStorage.getItem('server-host') || '';
export const setApiHost = (newHost: string) => localStorage.setItem('server-host', newHost);
