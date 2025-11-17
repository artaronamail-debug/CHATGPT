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
    <div style={{ padding: '2rem', fontFamily: 'Arial' }}>
      <h1>🔍 Verificador de Claves Gemini</h1>
      <input
        type="text"
        value={clave}
        onChange={(e) => setClave(e.target.value)}
        placeholder="Ingresá tu clave Gemini"
        style={{ width: '300px', padding: '0.5rem', marginRight: '1rem' }}
      />
      <button onClick={verificar} style={{ padding: '0.5rem 1rem' }}>
        Verificar
      </button>

      {resultado && (
        <div style={{ marginTop: '2rem' }}>
          <h3>Resultado:</h3>
          <pre>{JSON.stringify(resultado, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;