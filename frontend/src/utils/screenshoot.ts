/**
 * Genera y descarga un PDF vertical (9:16) con texto simple sin librerías externas.
 * @param content Texto a incluir en el PDF
 * @param filename Nombre del archivo a descargar
 */
export const downloadVerticalPdf = (
  content: string,
  filename: string = 'story-format.pdf',
): void => {
  // 1. Setup dimensions for 9:16 ratio (360pt x 640pt is a good mobile base)
  const width = 360;
  const height = 640;

  // Escape PDF parentheses to avoid syntax errors
  const safeText = content.replace(/\(/g, '\\(').replace(/\)/g, '\\)');

  // 2. Define PDF Objects
  // Object 1: Catalog
  const obj1 = `1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n`;

  // Object 2: Page Tree
  const obj2 = `2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n`;

  // Object 3: Page (Defines 9:16 MediaBox)
  const obj3 = `3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 ${width} ${height}] /Resources << /Font << /F1 << /Type /Font /Subtype /Type1 /BaseFont /Helvetica >> >> >> /Contents 4 0 R >>\nendobj\n`;

  // Object 4: Content Stream (Text positioning)
  // Position text near top-left (20px from left, 600px from bottom)
  const streamData = `BT /F1 12 Tf 20 600 Td (${safeText}) Tj ET`;
  const obj4 = `4 0 obj\n<< /Length ${streamData.length} >>\nstream\n${streamData}\nendstream\nendobj\n`;

  // 3. Assemble Body
  const header = `%PDF-1.4\n`;
  const body = header + obj1 + obj2 + obj3 + obj4;

  // 4. Calculate Cross-Reference Table (XRef) offsets
  // This is mandatory for a valid PDF. We count bytes up to each object.
  const getOffset = (str: string) => str.length.toString().padStart(10, '0');

  const xrefOffset = body.length;
  const o1Pos = getOffset(header);
  const o2Pos = getOffset(header + obj1);
  const o3Pos = getOffset(header + obj1 + obj2);
  const o4Pos = getOffset(header + obj1 + obj2 + obj3);

  const xref = `xref\n0 5\n0000000000 65535 f \n${o1Pos} 00000 n \n${o2Pos} 00000 n \n${o3Pos} 00000 n \n${o4Pos} 00000 n \n`;

  const trailer = `trailer\n<< /Size 5 /Root 1 0 R >>\nstartxref\n${xrefOffset}\n%%EOF`;

  // 5. Create Blob and Trigger Download
  const pdfString = body + xref + trailer;
  const blob = new Blob([pdfString], { type: 'application/pdf' });
  const link = document.createElement('a');

  link.href = window.URL.createObjectURL(blob);
  link.download = filename;
  link.click();

  // Clean up
  window.URL.revokeObjectURL(link.href);
};
