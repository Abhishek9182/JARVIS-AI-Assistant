// import { Canvas, useFrame } from "@react-three/fiber";
// import { OrbitControls, Stars } from "@react-three/drei";
// import { useRef, useMemo, useState, useEffect } from "react";
// import * as THREE from "three";

// function EnergyParticles({ systemState }) {
//   const pointsRef = useRef();

//   const positions = useMemo(() => {
//     const count = 1800;
//     const data = new Float32Array(count * 3);

//     for (let i = 0; i < count; i++) {
//       const radius = 2.5 + Math.random() * 3.5;
//       const theta = Math.random() * Math.PI * 2;
//       const phi = Math.acos(2 * Math.random() - 1);

//       data[i * 3] =
//         radius * Math.sin(phi) * Math.cos(theta);

//       data[i * 3 + 1] =
//         radius * Math.sin(phi) * Math.sin(theta);

//       data[i * 3 + 2] =
//         radius * Math.cos(phi);
//     }

//     return data;
//   }, []);

//   useFrame((state, delta) => {
//   if (!pointsRef.current) return;

//   let particleSpeed = 0.035;

//   if (systemState === "LISTENING") {
//     particleSpeed = 0.08;
//   }

//   if (systemState === "THINKING") {
//     particleSpeed = 0.16;
//   }

//   if (systemState === "RESPONDING") {
//     particleSpeed = 0.07;
//   }

//   if (systemState === "EXECUTING") {
//     particleSpeed = 0.25;
//   }

//   pointsRef.current.rotation.y +=
//     delta * particleSpeed;

//   pointsRef.current.rotation.x +=
//     delta * particleSpeed * 0.35;

//   const time = state.clock.getElapsedTime();

//   pointsRef.current.material.opacity =
//     0.45 + Math.sin(time * 1.5) * 0.15;
// });

//   return (
//     <points ref={pointsRef}>
//       <bufferGeometry>
//         <bufferAttribute
//           attach="attributes-position"
//           count={positions.length / 3}
//           array={positions}
//           itemSize={3}
//         />
//       </bufferGeometry>

//       <pointsMaterial
//         color="#00dfff"
//         size={0.025}
//         transparent
//         opacity={0.55}
//         sizeAttenuation
//         depthWrite={false}
//       />
//     </points>
//   );
// }



// //**Add the voice wave component**

// function VoiceWave({ active }) {
//   const canvasRef = useRef(null);
//   const animationRef = useRef(null);
//   const audioContextRef = useRef(null);
//   const analyserRef = useRef(null);
//   const streamRef = useRef(null);

//   useEffect(() => {
//     if (!active) {
//       if (animationRef.current) {
//         cancelAnimationFrame(animationRef.current);
//       }

//       if (audioContextRef.current) {
//         audioContextRef.current.close();
//         audioContextRef.current = null;
//       }

//       if (streamRef.current) {
//         streamRef.current
//           .getTracks()
//           .forEach((track) => track.stop());

//         streamRef.current = null;
//       }

//       return;
//     }

//     let cancelled = false;

//     const startMicrophone = async () => {
//       try {
//         const stream =
//           await navigator.mediaDevices.getUserMedia({
//             audio: true,
//           });

//         if (cancelled) {
//           stream.getTracks().forEach((track) =>
//             track.stop()
//           );
//           return;
//         }

//         streamRef.current = stream;

//         const AudioContext =
//           window.AudioContext ||
//           window.webkitAudioContext;

//         const audioContext = new AudioContext();

//         audioContextRef.current = audioContext;

//         const analyser =
//           audioContext.createAnalyser();

//         analyser.fftSize = 256;
//         analyser.smoothingTimeConstant = 0.8;

//         analyserRef.current = analyser;

//         const source =
//           audioContext.createMediaStreamSource(
//             stream
//           );

//         source.connect(analyser);

//         const canvas = canvasRef.current;

//         if (!canvas) return;

//         const ctx = canvas.getContext("2d");

//         const dataArray =
//           new Uint8Array(analyser.frequencyBinCount);

//         const draw = () => {
//           if (!canvasRef.current) return;

//           const width = canvas.width;
//           const height = canvas.height;

//           ctx.clearRect(
//             0,
//             0,
//             width,
//             height
//           );

//           analyser.getByteFrequencyData(
//             dataArray
//           );

//           ctx.beginPath();

//           const barWidth =
//             width / dataArray.length;

//           let x = 0;

//           for (
//             let i = 0;
//             i < dataArray.length;
//             i++
//           ) {
//             const value = dataArray[i];

//             const barHeight =
//               (value / 255) * height;

//             const y =
//               height / 2 - barHeight / 2;

//             ctx.moveTo(x, y);

//             ctx.lineTo(
//               x,
//               y + barHeight
//             );

//             x += barWidth;
//           }

//           ctx.strokeStyle =
//             "rgba(0, 234, 255, 0.9)";

//           ctx.lineWidth = 2;

//           ctx.shadowBlur = 12;

//           ctx.shadowColor = "#00eaff";

//           ctx.stroke();

//           animationRef.current =
//             requestAnimationFrame(draw);
//         };

//         draw();
//       } catch (error) {
//         console.error(
//           "Microphone access failed:",
//           error
//         );
//       }
//     };

//     startMicrophone();

//     return () => {
//       cancelled = true;

//       if (animationRef.current) {
//         cancelAnimationFrame(
//           animationRef.current
//         );
//       }

//       if (streamRef.current) {
//         streamRef.current
//           .getTracks()
//           .forEach((track) => track.stop());

//         streamRef.current = null;
//       }

//       if (audioContextRef.current) {
//         audioContextRef.current.close();

//         audioContextRef.current = null;
//       }
//     };
//   }, [active]);

//   return (
//     <canvas
//       ref={canvasRef}
//       className="voice-wave"
//       width={600}
//       height={80}
//     />
//   );
// }

// function Core({ systemState }) {
//   const coreRef = useRef();
//   const innerRef = useRef();
//   const ring1Ref = useRef();
//   const ring2Ref = useRef();
//   const ring3Ref = useRef();

//   useFrame((state, delta) => {
//   const time = state.clock.getElapsedTime();

//   let speed = 0.35;
//   let pulseSpeed = 2.5;

//   if (systemState === "LISTENING") {
//     speed = 0.9;
//     pulseSpeed = 5;
//   }

//   if (systemState === "THINKING") {
//     speed = 1.5;
//     pulseSpeed = 7;
//   }

//   if (systemState === "RESPONDING") {
//     speed = 0.7;
//     pulseSpeed = 4;
//   }

//   if (systemState === "EXECUTING") {
//     speed = 2.2;
//     pulseSpeed = 9;
//   }

//   if (coreRef.current) {
//     coreRef.current.rotation.x = time * speed * 0.6;
//     coreRef.current.rotation.y = time * speed;
//     coreRef.current.rotation.z = time * speed * 0.25;
//   }

//   if (innerRef.current) {
//     const scale =
//       1 + Math.sin(time * pulseSpeed) * 0.1;

//     innerRef.current.scale.setScalar(scale);
//   }

//   if (ring1Ref.current) {
//     ring1Ref.current.rotation.x += delta * speed;
//     ring1Ref.current.rotation.y += delta * speed * 0.5;
//   }

//   if (ring2Ref.current) {
//     ring2Ref.current.rotation.x -= delta * speed * 0.7;
//     ring2Ref.current.rotation.z += delta * speed;
//   }

//   if (ring3Ref.current) {
//     ring3Ref.current.rotation.y += delta * speed * 0.5;
//     ring3Ref.current.rotation.z -= delta * speed * 0.8;
//   }
// });

//   return (
//     <group>
//       {/* Outer energy shell */}
//       <mesh ref={coreRef}>
//         <icosahedronGeometry args={[1.25, 3]} />
//         <meshStandardMaterial
//           color="#00dfff"
//           emissive="#0088ff"
//           emissiveIntensity={3}
//           metalness={0.9}
//           roughness={0.1}
//           wireframe
//         />
//       </mesh>

//       {/* Inner energy sphere */}
//       <mesh ref={innerRef}>
//         <sphereGeometry args={[0.7, 32, 32]} />
//         <meshBasicMaterial
//           color="#bfffff"
//           transparent
//           opacity={0.75}
//         />
//       </mesh>

//       {/* Inner ring */}
//       <mesh ref={ring1Ref} rotation={[Math.PI / 2, 0, 0]}>
//         <torusGeometry args={[1.45, 0.018, 12, 160]} />
//         <meshBasicMaterial color="#00ffff" />
//       </mesh>

//       {/* Middle ring */}
//       <mesh ref={ring2Ref} rotation={[0.5, 0.8, 0]}>
//         <torusGeometry args={[1.8, 0.022, 12, 160]} />
//         <meshBasicMaterial color="#008cff" />
//       </mesh>

//       {/* Outer ring */}
//       <mesh ref={ring3Ref} rotation={[1.1, 0.2, 0.4]}>
//         <torusGeometry args={[2.15, 0.014, 12, 160]} />
//         <meshBasicMaterial color="#00eaff" />
//       </mesh>

//       {/* Energy lights */}
//       <pointLight
//         color="#00eaff"
//         intensity={30}
//         distance={8}
//       />

//       <pointLight
//         color="#0066ff"
//         intensity={18}
//         distance={7}
//         position={[2, 2, 2]}
//       />

//       <pointLight
//         color="#00ffff"
//         intensity={12}
//         distance={6}
//         position={[-2, -1, 1]}
//       />
//     </group>
//   );
// }


// export default function App() {
//   const [systemState, setSystemState] =
//     useState("IDLE");

//   const [micActive, setMicActive] =
//     useState(false);

//   return (
//     <div className="jarvis">
//       <div className="header">
//         <div>
//           <div className="title">J.A.R.V.I.S.</div>
//           <div className="subtitle">
//             JUST A RATHER VERY INTELLIGENT SYSTEM
//           </div>
//         </div>

//         <div className="status">
//           <span className="status-dot"></span>
//           SYSTEM ONLINE
//         </div>
//       </div>

//       <main>
//         <div className="side-panel left-panel">
//           <div className="panel-title">SYSTEM</div>

//           <div className="menu-item active">HOME</div>
//           <div className="menu-item">CHAT</div>
//           <div className="menu-item">VOICE</div>
//           <div className="menu-item">TASKS</div>
//           <div className="menu-item">AUTOMATION</div>
//           <div className="menu-item">APPS</div>
//           <div className="menu-item">SETTINGS</div>
//         </div>

//         <section className="core-section">
//           <div className="scan-line"></div>

//           <div className="hud-corner top-left"></div>
//           <div className="hud-corner top-right"></div>
//           <div className="hud-corner bottom-left"></div>
//           <div className="hud-corner bottom-right"></div>

//           <div className="state">
//             {systemState}
//           </div>

//           <div className="core-container">
//             <Canvas camera={{ position: [0, 0, 7], fov: 45 }}>
//               <ambientLight intensity={0.2} />

//               <Stars
//                 radius={80}
//                 depth={50}
//                 count={2500}
//                 factor={3}
//                 saturation={0}
//                 fade
//                 speed={0.4}
//               />

//               <EnergyParticles systemState={systemState} />

//               <Core systemState={systemState} />

//               <OrbitControls
//                 enableZoom={false}
//                 enablePan={false}
//                 autoRotate={false}
//               />
//             </Canvas>
//           </div>

//           <h1>HOW CAN I ASSIST?</h1>

//           <p className="hint">
//             Voice interface ready
//           </p>

//           <div className="state-controls">
//             <button
//               onClick={() => {
//                 setSystemState("IDLE");
//                 setMicActive(false);
//               }}
//             >
//               IDLE
//             </button>

//             <button
//               onClick={() => {
//                 setSystemState("LISTENING");
//                 setMicActive(true);
//               }}
//             >
//               LISTEN
//             </button>

//             <button onClick={() => setSystemState("THINKING")}>
//               THINK
//             </button>

//             <button onClick={() => setSystemState("RESPONDING")}>
//               RESPOND
//             </button>

//             <button onClick={() => setSystemState("EXECUTING")}>
//               EXECUTE
//             </button>
//           </div>

//           <VoiceWave active={micActive} />

//           <div className="command-box">
//             <span className="mic">◉</span>
//             <span>Awaiting command...</span>
//           </div>
//         </section>

//         <div className="side-panel right-panel">
//           <div className="panel-title">SYSTEM STATUS</div>

//           <div className="status-row">
//             <span>CORE</span>
//             <span className="online">ONLINE</span>
//           </div>

//           <div className="status-row">
//             <span>VOICE</span>
//             <span className="online">READY</span>
//           </div>

//           <div className="status-row">
//             <span>AI ENGINE</span>
//             <span className="online">ACTIVE</span>
//           </div>

//           <div className="status-row">
//             <span>NETWORK</span>
//             <span className="online">CONNECTED</span>
//           </div>

//           <div className="panel-title quick-title">
//             QUICK ACTIONS
//           </div>

//           <button>OPEN CHAT</button>
//           <button>VOICE MODE</button>
//           <button>RUN TASK</button>
//         </div>
//       </main>
//     </div>
//   );
// }

import { useEffect, useRef, useState } from "react";
import { Canvas, useFrame } from "@react-three/fiber";
import { Stars } from "@react-three/drei";
import * as THREE from "three";


// ============================================================
// JARVIS CORE
// ============================================================

function Core({ systemState }) {

  const coreRef = useRef();
  const ring1 = useRef();
  const ring2 = useRef();
  const ring3 = useRef();

  const speedMap = {
    IDLE: 0.15,
    LISTENING: 0.8,
    THINKING: 1.5,
    RESPONDING: 1.0,
    EXECUTING: 2.2,
    ERROR: 0.3,
  };

  const pulseMap = {
    IDLE: 1,
    LISTENING: 1.15,
    THINKING: 1.3,
    RESPONDING: 1.2,
    EXECUTING: 1.45,
    ERROR: 0.9,
  };

  useFrame((state) => {

    const t = state.clock.getElapsedTime();

    const speed = speedMap[systemState] || 0.15;
    const pulse = pulseMap[systemState] || 1;

    if (coreRef.current) {

      coreRef.current.rotation.x += 0.003 * speed;
      coreRef.current.rotation.y += 0.006 * speed;

      const scale =
        1 +
        Math.sin(t * 2.5 * speed) * 0.04 * pulse;

      coreRef.current.scale.set(
        scale,
        scale,
        scale
      );
    }

    if (ring1.current) {
      ring1.current.rotation.x += 0.004 * speed;
      ring1.current.rotation.y += 0.002 * speed;
    }

    if (ring2.current) {
      ring2.current.rotation.y -= 0.005 * speed;
      ring2.current.rotation.z += 0.003 * speed;
    }

    if (ring3.current) {
      ring3.current.rotation.x -= 0.003 * speed;
      ring3.current.rotation.z += 0.004 * speed;
    }
  });

  return (
    <group>

      {/* Main energy sphere */}
      <mesh ref={coreRef}>

        <icosahedronGeometry args={[1.4, 2]} />

        <meshStandardMaterial
          color="#00d9ff"
          wireframe
          emissive="#00aaff"
          emissiveIntensity={3}
        />

      </mesh>


      {/* Inner glowing sphere */}
      <mesh>

        <sphereGeometry args={[0.75, 32, 32]} />

        <meshStandardMaterial
          color="#003b55"
          emissive="#00d9ff"
          emissiveIntensity={4}
          transparent
          opacity={0.75}
        />

      </mesh>


      {/* Energy rings */}

      <mesh ref={ring1.current}>
        <torusGeometry args={[2.0, 0.025, 16, 128]} />
        <meshBasicMaterial color="#00eaff" />
      </mesh>

      <mesh
        ref={ring2.current}
        rotation={[Math.PI / 2, 0, 0]}
      >
        <torusGeometry args={[2.35, 0.018, 16, 128]} />
        <meshBasicMaterial color="#0088ff" />
      </mesh>

      <mesh
        ref={ring3.current}
        rotation={[0, Math.PI / 3, 0]}
      >
        <torusGeometry args={[2.7, 0.012, 16, 128]} />
        <meshBasicMaterial color="#00c8ff" />
      </mesh>


      {/* Lights */}

      <pointLight
        color="#00eaff"
        intensity={systemState === "THINKING" ? 8 : 5}
        distance={10}
      />

      <pointLight
        color="#0066ff"
        intensity={4}
        position={[3, 2, 2]}
      />

      <pointLight
        color="#00ffff"
        intensity={3}
        position={[-3, -2, -2]}
      />

    </group>
  );
}


// ============================================================
// PARTICLES
// ============================================================

function EnergyParticles({ systemState }) {

  const pointsRef = useRef();

  const count = 1800;

  const positions = new Float32Array(count * 3);

  for (let i = 0; i < count; i++) {

    const radius = 4 + Math.random() * 7;

    const theta =
      Math.random() * Math.PI * 2;

    const phi =
      Math.acos(
        2 * Math.random() - 1
      );

    positions[i * 3] =
      radius *
      Math.sin(phi) *
      Math.cos(theta);

    positions[i * 3 + 1] =
      radius *
      Math.sin(phi) *
      Math.sin(theta);

    positions[i * 3 + 2] =
      radius *
      Math.cos(phi);
  }

  useFrame((state) => {

    const t = state.clock.getElapsedTime();

    const speed =
      systemState === "EXECUTING"
        ? 0.0018
        : systemState === "THINKING"
        ? 0.0012
        : 0.0004;

    if (pointsRef.current) {

      pointsRef.current.rotation.y =
        t * speed;

      pointsRef.current.rotation.x =
        t * speed * 0.5;
    }
  });

  return (
    <points ref={pointsRef}>

      <bufferGeometry>

        <bufferAttribute
          attach="attributes-position"
          count={count}
          array={positions}
          itemSize={3}
        />

      </bufferGeometry>

      <pointsMaterial
        size={0.025}
        color="#00d9ff"
        transparent
        opacity={0.7}
      />

    </points>
  );
}


// ============================================================
// VOICE WAVEFORM
// ============================================================

function VoiceWave({ active }) {

  const canvasRef = useRef();

  useEffect(() => {

    if (!active) return;

    let animationFrame;
    let audioContext;
    let analyser;
    let stream;

    const startAudio = async () => {

      try {

        stream =
          await navigator.mediaDevices.getUserMedia({
            audio: true,
          });

        audioContext =
          new AudioContext();

        const source =
          audioContext.createMediaStreamSource(
            stream
          );

        analyser =
          audioContext.createAnalyser();

        analyser.fftSize = 256;

        source.connect(analyser);

        const data =
          new Uint8Array(
            analyser.frequencyBinCount
          );

        const canvas =
          canvasRef.current;

        const ctx =
          canvas.getContext("2d");

        const draw = () => {

          animationFrame =
            requestAnimationFrame(draw);

          analyser.getByteTimeDomainData(data);

          ctx.clearRect(
            0,
            0,
            canvas.width,
            canvas.height
          );

          ctx.beginPath();

          const sliceWidth =
            canvas.width /
            data.length;

          let x = 0;

          for (
            let i = 0;
            i < data.length;
            i++
          ) {

            const v =
              data[i] / 128.0;

            const y =
              (v * canvas.height) / 2;

            if (i === 0) {
              ctx.moveTo(x, y);
            } else {
              ctx.lineTo(x, y);
            }

            x += sliceWidth;
          }

          ctx.strokeStyle =
            "#00eaff";

          ctx.lineWidth = 2;

          ctx.stroke();
        };

        draw();

      } catch (error) {

        console.error(
          "Microphone error:",
          error
        );
      }
    };

    startAudio();

    return () => {

      cancelAnimationFrame(
        animationFrame
      );

      if (stream) {

        stream
          .getTracks()
          .forEach(track =>
            track.stop()
          );
      }

      if (audioContext) {
        audioContext.close();
      }
    };

  }, [active]);

  return (
    <canvas
      ref={canvasRef}
      className="voice-wave"
      width="500"
      height="100"
    />
  );
}


// ============================================================
// MAIN APP
// ============================================================

export default function App() {

  const [systemState, setSystemState] =
    useState("IDLE");

  const [command, setCommand] =
    useState("");

  const [reply, setReply] =
    useState("JARVIS AI SYSTEM READY.");

  const [processing, setProcessing] =
    useState(false);

  const [micActive, setMicActive] =
    useState(false);


  // ==========================================================
  // SEND COMMAND TO PYTHON
  // ==========================================================

  const sendCommand = async () => {

    const text =
      command.trim();

    if (!text || processing) {
      return;
    }

    setProcessing(true);

    setSystemState("THINKING");

    setReply(
      "PROCESSING COMMAND..."
    );

    try {

      const response =
        await fetch(
          "http://127.0.0.1:5001/api/command",
          {
            method: "POST",

            headers: {
              "Content-Type":
                "application/json",
            },

            body: JSON.stringify({
              command: text,
            }),
          }
        );

      const data =
        await response.json();

      if (!response.ok || !data.success) {

        throw new Error(
          data.error ||
          "JARVIS API ERROR"
        );
      }

      setSystemState("RESPONDING");

      setReply(
        data.reply ||
        "Command completed."
      );

      setCommand("");

      setTimeout(() => {
        setSystemState("IDLE");
      }, 1800);

    } catch (error) {

      console.error(
        "JARVIS API ERROR:",
        error
      );

      setSystemState("ERROR");

      setReply(
        "I'M SORRY, SIR. I COULD NOT CONNECT TO THE JARVIS CORE."
      );

    } finally {

      setProcessing(false);
    }
  };


  // ==========================================================
  // ENTER KEY
  // ==========================================================

  const handleKeyDown = (event) => {

    if (event.key === "Enter") {
      sendCommand();
    }
  };


  return (

    <div className="jarvis">

      {/* ====================================================
          HEADER
      ==================================================== */}

      <header className="topbar">

        <div className="logo">
          J.A.R.V.I.S
        </div>

        <div className="system-online">
          ● SYSTEM ONLINE
        </div>

      </header>


      {/* ====================================================
          LEFT PANEL
      ==================================================== */}

      <aside className="left-panel">

        <div className="panel-title">
          SYSTEM
        </div>

        <div className="menu-item active">
          ◈ CORE
        </div>

        <div className="menu-item">
          ◈ AI ENGINE
        </div>

        <div className="menu-item">
          ◈ AUTOMATION
        </div>

        <div className="menu-item">
          ◈ NETWORK
        </div>

        <div className="menu-item">
          ◈ SECURITY
        </div>

      </aside>


      {/* ====================================================
          CENTER
      ==================================================== */}

      <main className="center-stage">

        <div className="scan-line"></div>

        <div className="hud-corner top-left"></div>
        <div className="hud-corner top-right"></div>
        <div className="hud-corner bottom-left"></div>
        <div className="hud-corner bottom-right"></div>


        <Canvas
          camera={{
            position: [0, 0, 9],
            fov: 55,
          }}
        >

          <ambientLight intensity={0.15} />

          <Stars
            radius={50}
            depth={30}
            count={2000}
            factor={2}
            saturation={0}
            fade
            speed={0.5}
          />

          <EnergyParticles
            systemState={systemState}
          />

          <Core
            systemState={systemState}
          />

        </Canvas>


        <div className="core-label">

          <div className="state-label">
            {systemState}
          </div>

          <div className="core-name">
            J.A.R.V.I.S CORE
          </div>

        </div>


        <VoiceWave
          active={micActive}
        />

      </main>


      {/* ====================================================
          RIGHT PANEL
      ==================================================== */}

      <aside className="right-panel">

        <div className="panel-title">
          SYSTEM STATUS
        </div>

        <div className="status-row">
          <span>CORE</span>
          <strong>ONLINE</strong>
        </div>

        <div className="status-row">
          <span>AI ENGINE</span>
          <strong>ACTIVE</strong>
        </div>

        <div className="status-row">
          <span>VOICE</span>
          <strong>
            {micActive
              ? "LISTENING"
              : "READY"}
          </strong>
        </div>

        <div className="status-row">
          <span>STATE</span>
          <strong>
            {systemState}
          </strong>
        </div>


        <div className="panel-title quick-title">
          QUICK ACTIONS
        </div>


        <button
          onClick={() => {
            setSystemState("IDLE");
            setMicActive(false);
          }}
        >
          IDLE
        </button>


        <button
          onClick={() => {
            setSystemState("LISTENING");
            setMicActive(true);
          }}
        >
          LISTEN
        </button>


        <button
          onClick={() =>
            setSystemState("THINKING")
          }
        >
          THINK
        </button>


        <button
          onClick={() =>
            setSystemState("RESPONDING")
          }
        >
          RESPOND
        </button>


        <button
          onClick={() =>
            setSystemState("EXECUTING")
          }
        >
          EXECUTE
        </button>


        <button
          onClick={() => {
            setSystemState("IDLE");
            setMicActive(false);
          }}
        >
          STOP LISTENING
        </button>

      </aside>


      {/* ====================================================
          COMMAND CONSOLE
      ==================================================== */}

      <section className="command-console">

        <div className="reply-box">

          <div className="reply-label">
            JARVIS RESPONSE
          </div>

          <div className="reply-text">
            {reply}
          </div>

        </div>


        <div className="command-row">

          <span className="prompt">
            &gt;
          </span>

          <input
            value={command}
            onChange={(e) =>
              setCommand(e.target.value)
            }
            onKeyDown={handleKeyDown}
            placeholder="ENTER COMMAND..."
            disabled={processing}
          />

          <button
            onClick={sendCommand}
            disabled={processing}
          >
            {processing
              ? "PROCESSING"
              : "EXECUTE"}
          </button>

        </div>

      </section>

    </div>
  );
}