/**
 * Convierte un objeto File a una cadena de texto Base64.
 *
 * @param {File} file - El archivo de imagen a convertir.
 * @returns {Promise<string>} Una promesa que resuelve con la cadena Base64 (Data URL).
 */
export function fileToBase64(file: File): Promise<string> {
    // Aseguramos que solo archivos de imagen sean procesados (opcional, pero útil)
    if (!file.type.startsWith('image/')) {
        return Promise.reject(new Error('El archivo seleccionado no es una imagen.'));
    }

    // Retorna una promesa para manejar la operación asíncrona
    return new Promise((resolve, reject) => {
        const reader = new FileReader();

        // Si la lectura es exitosa
        reader.onload = () => {
            // El resultado siempre será una cadena Data URL para readAsDataURL
            resolve(reader.result as string);
        };

        // Si ocurre un error
        reader.onerror = (error) => {
            // eslint-disable-next-line @typescript-eslint/prefer-promise-reject-errors
            reject(error);
        };

        // Lee el archivo como una Data URL (Base64)
        reader.readAsDataURL(file);
    });
}
