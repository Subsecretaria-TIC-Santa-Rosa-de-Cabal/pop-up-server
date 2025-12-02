interface FileUploadOptions {
  url: string;
  file: File;
  fields?: { key?: string };
}

export const apiUploadFiles = async ({
  url,
  file,
  fields = {},
}: FileUploadOptions): Promise<unknown> => {
  try {
    const formData = new FormData();

    for (const [key, value] of Object.entries(fields)) {
      formData.append(key, value);
    }

    formData.append('file', file);

    const response = await fetch(`${url}`, {
      method: 'POST',
      body: formData,
    });

    if (response.status !== 204) {
      throw new Error('Upload failed');
    }

    const data = await response.json();

    return data;
  } catch (e) {
    if (typeof e === 'object' && e !== null && 'status' in e) {
      if (e.status && e.status == 204) {
        return true;
      } else {
        throw e;
      }
    }
  }
};
