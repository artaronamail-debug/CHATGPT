import React, { useState } from 'react';
import { diagnosticoGemini } from './api';

function App() {
  const [clave, setClave] = useState('');
  const [resultado, setResultado] = useState(null);

  const verificar = async () => {
    const data = await diagnosticoGemini(clave);
    setResultado(data);
  };

  return (
    <div>
      <h1>Verificador de Claves Gemini</h1>
      <input
        type="text"
        value={clave}
        onChange={(e) => setClave(e.target.value)}
        placeholder="Ingresá tu clave Gemini"
      />
      <button onClick={verificar}>Verificar</button>

      {resultado && (
        <pre>{JSON.stringify(resultado, null, 2)}</pre>
      )}
    </div>
  );
}

export default App;