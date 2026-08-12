import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import { describe, expect, it } from "vitest";

const css = readFileSync(resolve(process.cwd(), "src/styles/globals.css"), "utf8");

describe("mobile layout CSS contract", () => {
  it("keeps the 320px ranking in two rows without page-level horizontal overflow", () => {
    const mobileStart = css.indexOf("@media (max-width: 640px)");
    const mobileEnd = css.indexOf("@media (prefers-reduced-motion", mobileStart);
    const mobileRules = css.slice(mobileStart, mobileEnd);

    expect(mobileStart).toBeGreaterThanOrEqual(0);
    expect(mobileRules).toMatch(
      /\.sector-ranking button\s*\{[^}]*grid-template-areas:\s*"rank name score change"\s*"rank lifecycle phase change"/,
    );
    expect(css).toMatch(/\.rotation-page\s*\{[^}]*overflow-x:\s*hidden/);
    expect(css).toMatch(/\.lifecycle-bands\s*\{[^}]*overflow-x:\s*auto/);
  });

  it("keeps native date options legible and the Lifecycle toggle compact", () => {
    expect(css).toMatch(/\.filter-field select option\s*\{[^}]*background:\s*#0c192b[^}]*color:\s*var\(--text\)/);
    expect(css).toMatch(/\.filter-field--checkbox input\[type="checkbox"\]\s*\{[^}]*width:\s*16px[^}]*height:\s*16px/);
  });
  it("styles each trading calendar status independently", () => {
    expect(css).toMatch(/\.trading-calendar__day\[data-date-status="snapshot"\]/);
    expect(css).toMatch(/\.trading-calendar__day\[data-date-status="pending"\]/);
    expect(css).toMatch(/\.trading-calendar__day\[data-date-status="closed"\]/);
  });
  it("positions the trading calendar popover outside the filter layout", () => {
    expect(css).toMatch(/\.trading-calendar-filter\s*\{[^}]*position:\s*relative/);
    expect(css).toMatch(/\.trading-calendar-popover\s*\{[^}]*position:\s*absolute[^}]*z-index:\s*\d+/);
    expect(css).toMatch(/\.trading-calendar-trigger\s*\{/);
  });

  it("keeps the filter stacking context above the following market summary", () => {
    expect(css).toMatch(/\.rotation-filters\s*\{[^}]*position:\s*relative[^}]*z-index:\s*2/);
  });

  it("reserves the calendar trigger width in the second desktop filter track", () => {
    expect(css).toMatch(/\.rotation-filters\s*\{[^}]*grid-template-columns:\s*minmax\(150px, \.8fr\) minmax\(238px, \.7fr\)/);
  });

  it("gives Lifecycle its own wrapping desktop row while keeping ranking change visible", () => {
    expect(css).toMatch(/\.rotation-workspace\s*\{[^}]*grid-template-columns:\s*minmax\(0, 1fr\) 390px/);
    expect(css).toMatch(/\.sector-ranking button\s*\{[^}]*grid-template-areas:\s*"rank name phase score change"\s*"rank lifecycle lifecycle lifecycle lifecycle"/);
    expect(css).toMatch(/\.lifecycle-pill\s*\{[^}]*flex-wrap:\s*wrap[^}]*white-space:\s*normal/);
    expect(css).toMatch(/\.lifecycle-pill__segment\s*\{[^}]*overflow-wrap:\s*anywhere/);
    expect(css).toMatch(/\.sector-ranking em\s*\{[^}]*white-space:\s*nowrap/);
  });

  it("renders the drawer market context as a three-tier dark surface", () => {
    expect(css).toMatch(/\.detail-market-context\s*\{[^}]*display:\s*grid[^}]*gap:\s*\d+px[^}]*margin-top:\s*18px[^}]*padding:\s*15px[^}]*border:\s*1px solid var\(--line\)[^}]*border-radius:\s*12px[^}]*background:\s*rgba\(7, 18, 32, \.76\)/);
    expect(css).toMatch(/\.detail-market-context > p\s*\{[^}]*font-size:\s*9px/);
    expect(css).toMatch(/\.detail-market-context strong\s*\{[^}]*font-size:\s*14px/);
    expect(css).toMatch(/\.detail-market-context span\s*\{[^}]*font-size:\s*10px/);
  });

  it("lays out the combination conclusion metrics responsively without relying on tone color", () => {
    expect(css).toMatch(/\.detail-combination-conclusion\s*\{[^}]*border-radius:\s*12px/);
    expect(css).toMatch(/\.detail-combination-conclusion\.tone-positive\s*\{/);
    expect(css).toMatch(/\.detail-combination-conclusion\.tone-watch\s*\{/);
    expect(css).toMatch(/\.detail-combination-conclusion\.tone-risk\s*\{/);
    expect(css).toMatch(/\.detail-combination-conclusion\.tone-neutral\s*\{/);
    expect(css).toMatch(/\.detail-lifecycle-metrics\s*\{[^}]*grid-template-columns:\s*repeat\(2, minmax\(0, 1fr\)\)/);
    expect(css).toMatch(/\.detail-lifecycle-metrics strong\s*\{[^}]*overflow-wrap:\s*anywhere/);
    const mobileStart = css.lastIndexOf("@media (max-width: 640px)");
    const mobileRules = css.slice(mobileStart);
    expect(mobileRules).toMatch(/\.detail-lifecycle-metrics\s*\{[^}]*grid-template-columns:\s*1fr/);
  });
});
