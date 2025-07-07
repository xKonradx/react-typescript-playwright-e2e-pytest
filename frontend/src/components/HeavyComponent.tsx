import React, { useMemo } from "react";

function heavyCalculation() {
  let sum = 0;
  for (let i = 0; i < 1e7; i++) sum += Math.sqrt(i);
  return sum;
}

const HeavyComponent: React.FC = React.memo(() => {
  const value = useMemo(() => heavyCalculation(), []);
  return (
    <div className="p-4 bg-base-200 rounded mt-4">
      <strong>Wynik ciężkiego obliczenia:</strong> {value}
    </div>
  );
});

export default HeavyComponent;
