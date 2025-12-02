export const translateErrorCodeToMessage = (errorCode?: number | string): string => {
  const errorMessages: { [key: string]: string } = {
    '1001': 'Credenciales incorrectas',
  };

  return errorMessages[String(errorCode)] || `Error desconocido: ${errorCode}`;
};
