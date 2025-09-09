---
title: Resources
date: 2022-10-24

type: landing

sections:
  - block: markdown
    content:
      title: Lab Resources
      subtitle: 'Tools and Infrastructure for Research'
      text: |
        <div style="text-align: center; margin-bottom: 2rem;">
          <p style="font-size: 1.1rem; color: #6b7280;">Access lab computing resources and monitoring tools</p>
        </div>
        
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; margin-top: 2rem;">
          <div style="background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 12px; padding: 2rem; text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">🖥️</div>
            <h3 style="color: #1f2937; margin-bottom: 1rem;">GPU Monitor</h3>
            <p style="color: #6b7280; margin-bottom: 1.5rem;">Real-time monitoring of lab GPU resources and usage statistics</p>
            <a href="#gpu-monitor-container" style="background-color: #3b82f6; color: white; padding: 0.75rem 1.5rem; text-decoration: none; border-radius: 8px; font-weight: 500;">View GPU Status</a>
          </div>
          
          <div style="background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 12px; padding: 2rem; text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">📚</div>
            <h3 style="color: #1f2937; margin-bottom: 1rem;">Documentation</h3>
            <p style="color: #6b7280; margin-bottom: 1.5rem;">Lab guides, tutorials, and research documentation</p>
            <a href="#" style="background-color: #10b981; color: white; padding: 0.75rem 1.5rem; text-decoration: none; border-radius: 8px; font-weight: 500;">Coming Soon</a>
          </div>
          
          <div style="background: #f9fafb; border: 1px solid #e5e7eb; border-radius: 12px; padding: 2rem; text-align: center;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">🔧</div>
            <h3 style="color: #1f2937; margin-bottom: 1rem;">Tools</h3>
            <p style="color: #6b7280; margin-bottom: 1.5rem;">Useful tools and utilities for research and development</p>
            <a href="#" style="background-color: #f59e0b; color: white; padding: 0.75rem 1.5rem; text-decoration: none; border-radius: 8px; font-weight: 500;">Coming Soon</a>
          </div>
        </div>
    design:
      columns: '1'
      spacing:
        padding: ['40px', '0', '40px', '0']
  - block: markdown
    content:
      title: GPU Monitor
      subtitle: Real-time monitoring of lab GPU resources
      text: |
        <div id="gpu-monitor-container">
          <div style="text-align: center; margin-bottom: 2rem;">
            <h2 style="color: #1f2937; margin-bottom: 0.5rem;">🖥️ GPU Usage Monitor</h2>
            <p style="color: #6b7280; font-size: 1.05rem;">Real-time monitoring of lab GPU resources</p>
            <div id="last-updated" style="color: #9ca3af; font-size: 0.9rem; margin-top: 0.5rem;">
              Last updated: <span id="update-time">Loading...</span>
            </div>
          </div>

          <div id="loading" style="text-align: center; padding: 2rem;">
            <div style="font-size: 1.1rem; color: #6b7280;">🔄 Loading GPU data...</div>
          </div>

          <div id="error-message" style="display: none; text-align: center; padding: 1.25rem; background-color: #fef2f2; border: 1px solid #fecaca; border-radius: 8px; margin: 1rem 0;">
            <div style="color: #dc2626; font-size: 1rem;">❌ Failed to load GPU data</div>
            <div style="color: #7f1d1d; font-size: 0.9rem; margin-top: 0.5rem;" id="error-details"></div>
          </div>

          <div id="servers-container" style="display: none;"></div>

          <div style="text-align: center; margin-top: 1.5rem;">
            <button id="refresh-btn" onclick="loadGPUData()" 
                    style="background-color: #3b82f6; color: white; padding: 0.6rem 1.25rem; border: none; border-radius: 8px; font-size: 0.95rem; cursor: pointer; transition: background-color 0.2s;">
              🔄 Refresh Data
            </button>
          </div>
        </div>

        <style>
        .server-card { background: white; border: 1px solid #e5e7eb; border-radius: 12px; padding: 1.25rem; margin-bottom: 1.25rem; box-shadow: 0 1px 3px rgba(0,0,0,.06); }
        .server-header { display: flex; align-items: center; justify-content: space-between; margin-bottom: 1rem; padding-bottom: 0.75rem; border-bottom: 1px solid #e5e7eb; }
        .server-title { font-size: 1.2rem; font-weight: 600; color: #1f2937; }
        .server-summary { background-color: #f3f4f6; padding: 0.35rem 0.75rem; border-radius: 6px; font-size: 0.85rem; color: #374151; }
        .gpu-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 0.9rem; }
        .gpu-card { border: 1px solid #d1d5db; border-radius: 8px; padding: 0.9rem; background-color: #fafafa; }
        .gpu-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.6rem; }
        .gpu-name { font-weight: 600; color: #374151; font-size: 0.9rem; }
        .gpu-id { background-color: #e5e7eb; padding: 0.2rem 0.5rem; border-radius: 4px; font-size: 0.8rem; color: #6b7280; }
        .usage-bars { margin-bottom: 0.8rem; }
        .usage-bar { margin-bottom: 0.6rem; }
        .usage-label { display: flex; justify-content: space-between; margin-bottom: 0.25rem; font-size: 0.83rem; color: #4b5563; }
        .progress-bar { width: 100%; height: 8px; background-color: #e5e7eb; border-radius: 4px; overflow: hidden; }
        .progress-fill { height: 100%; transition: width 0.3s ease; border-radius: 4px; }
        .utilization-low { background-color: #10b981; }
        .utilization-medium { background-color: #f59e0b; }
        .utilization-high { background-color: #ef4444; }
        .memory-low { background-color: #06b6d4; }
        .memory-medium { background-color: #f59e0b; }
        .memory-high { background-color: #ef4444; }
        .gpu-stats { display: flex; justify-content: space-between; font-size: 0.78rem; color: #6b7280; }
        #refresh-btn:hover { background-color: #2563eb; }
        .status-indicator { display: inline-block; width: 8px; height: 8px; border-radius: 50%; margin-right: 0.5rem; }
        .status-success { background-color: #10b981; }
        .status-error { background-color: #ef4444; }
        </style>

        <script>
        const API_ENDPOINT = '/api/gpu_status';
        function getUtilizationClass(u){ if(u<30) return 'utilization-low'; if(u<70) return 'utilization-medium'; return 'utilization-high'; }
        function getMemoryClass(p){ if(p<50) return 'memory-low'; if(p<80) return 'memory-medium'; return 'memory-high'; }
        function formatMemory(mb){ return mb>=1024 ? (mb/1024).toFixed(1)+ ' GB' : mb.toFixed(0)+' MB'; }
        function createGPUCard(g){ const mp=(g.mem_used/g.mem_total)*100; return `
          <div class="gpu-card">
            <div class="gpu-header"><div class="gpu-name">GPU ${'${g.id}'}</div><div class="gpu-id">${'${g.name}'}</div></div>
            <div class="usage-bars">
              <div class="usage-bar"><div class="usage-label"><span>Utilization</span><span><strong>${'${g.utilization.toFixed(1)}'}%</strong></span></div>
                <div class="progress-bar"><div class="progress-fill ${'${getUtilizationClass(g.utilization)}'}" style="width: ${'${g.utilization}'}%"></div></div>
              </div>
              <div class="usage-bar"><div class="usage-label"><span>Memory</span><span><strong>${'${mp.toFixed(1)}'}%</strong></span></div>
                <div class="progress-bar"><div class="progress-fill ${'${getMemoryClass(mp)}'}" style="width: ${'${mp}'}%"></div></div>
              </div>
            </div>
            <div class="gpu-stats"><span>Used: ${'${formatMemory(g.mem_used)}'}</span><span>Total: ${'${formatMemory(g.mem_total)}'}</span></div>
          </div>`; }
        function createServerCard(s){ const on=s.status==='success'; let c=`
          <div class="server-card">
            <div class="server-header">
              <div><div class="server-title"><span class="status-indicator ${'${on?"status-success":"status-error"}'}"></span>${'${s.hostname}'}:${'${s.port}'}</div></div>
              <div class="server-summary">${'${on?`${s.summary.used}/${s.summary.total} GPUs Online`:`Server Offline`}'}
              </div></div>`; if(on&&s.gpus&&s.gpus.length>0){ c+=`<div class="gpu-grid">${'${s.gpus.map(createGPUCard).join("")}'}</div>` } else if(!on){ c+=`<div style="text-align:center;padding:2rem;color:#6b7280;"><div style="font-size:1.05rem;">⚠️ Server is currently offline</div><div style="font-size:.9rem;margin-top:.5rem;">Unable to retrieve GPU information</div></div>` } return c+'</div>'; }
        async function loadGPUData(){ const loading=document.getElementById('loading'); const error=document.getElementById('error-message'); const box=document.getElementById('servers-container'); const time=document.getElementById('update-time'); const btn=document.getElementById('refresh-btn'); loading.style.display='block'; error.style.display='none'; box.style.display='none'; btn.disabled=true; btn.style.backgroundColor='#9ca3af';
          try{ const resp=await fetch(API_ENDPOINT); if(!resp.ok){ throw new Error(`HTTP error! status: ${'${resp.status}'}`) } const data=await resp.json(); const servers=Array.isArray(data)?data:[data]; loading.style.display='none'; box.innerHTML=servers.map(createServerCard).join(''); box.style.display='block'; time.textContent=(new Date()).toLocaleString(); }
          catch(e){ console.error('Error loading GPU data:', e); loading.style.display='none'; error.style.display='block'; document.getElementById('error-details').textContent=e.message; }
          finally{ btn.disabled=false; btn.style.backgroundColor='#3b82f6'; }
        }
        document.addEventListener('DOMContentLoaded', function(){ loadGPUData(); setInterval(loadGPUData, 30000); });
        </script>
    design:
      columns: '1'
      spacing:
        padding: ['20px', '0', '40px', '0']
---
